import pandas as pd

from evadb.functions.abstract.abstract_function import AbstractFunction
from evadb.catalog.catalog_type import NdArrayType
from evadb.functions.decorators.decorators import forward, setup
from evadb.functions.decorators.io_descriptors.data_types import PandasDataframe

class Llama(AbstractFunction):

  @property
  def name(self) -> str:
    return "Llama"
  
  @setup(cacheable=True, function_type="llama_integration", batchable=True)
  def setup(self):
    from llama_cpp import Llama
    self.model = Llama("evadb_data/models/gguf-model-f16.gguf")

  @forward(
    input_signatures=[
      PandasDataframe(
        columns=["query", "content"],
        column_types=[
          NdArrayType.STR,
          NdArrayType.STR,
        ],
        column_shapes=[(1,), (1,)],
      )
    ],
    output_signatures=[
      PandasDataframe(
        columns=["response"],
        column_types=[
          NdArrayType.STR,
        ],
        column_shapes=[(1,)],
      )
    ],
  )
  def forward(self, frames):
    queries = frames[frames.columns[0]]
    content = frames[frames.columns[0]]

    results = []

    for query in queries:
      prompt = query + content[0]
      response = self.model.create_completion(
        prompt=prompt,
        max_tokens=100
      )

      results.append(response["choices"][0]['text'])

    df = pd.DataFrame({"response": results})
    return df

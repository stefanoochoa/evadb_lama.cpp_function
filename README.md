# EvaDB Llama Function

## Background
For the first EvaDB project, I was exploring the topic of a LLaMa function. In my proposal, I outlined the idea for an AI-powered learning assistant. The end goal is to have an application that students can upload study materials, such as lecture slides, videos, textbook excerpts, etc and then ask questions, get study guides, flash cards, etc. Behind the scenes of this app, EvaDB would be used to process uploaded study materials, store them, and store chat logs and generated materials (such as study guides, practice quizzes, etc). LLaMa would be used to generate these materials (study guides, etc) and respond to the users questions. The integration between EvaDB and LLaMa would be done through a LLaMa function added to EvaDB.

## Project 1 Goal
For this project, I focused on the LLaMa function. This function would be invoked in an EvaDB query so that the LLaMa model can process the frames resulting from the query. For example, if the user uploaded some text from a text book, and wanted to have the app summarize it, the flow would be something like this: The user inputs ‘summarize material A’ , which gets converted to an EvaDB query. The query uses the LLaMa function, so that after we fetch the text, we then provide the prompt, ‘summarize’, and the text to the model. The model processes the information, and returns a response, which is propagated back to the user. 

## Progress
In this phase of the project, I was able to create a LLaMa function for EvaDB. This function takes a query, ie ‘summarize’, and some content, ie text book excerpt, and uses a LLaMa model to process the information and return a response. The model used in my testing was the 7B model obtained following these instructions: https://github.com/cocktailpeanut/dalai#quickstart.
To interface with the model, I utilized the lama.cpp library https://github.com/ggerganov/llama.cpp and the python bindings I found here https://github.com/abetlen/llama-cpp-python.


## Usage
1. Install EvaDB: [EvaDB Documentation](https://evadb.readthedocs.io/en/stable/source/overview/getting-started.html)
2. Place ```llama.py``` in ```evadb_data/functions```
3. Follow [these instructions](https://github.com/cocktailpeanut/dalai#quickstart) to install the 7B model.
4. Follow [these instructions](https://github.com/abetlen/llama-cpp-python#:~:text=Starting%20with%20version%200.1.79%20the%20model%20format%20has%20changed%20from%20ggmlv3%20to%20gguf.%20Old%20model%20files%20can%20be%20converted%20using%20the%20convert%2Dllama%2Dggmlv3%2Dto%2Dgguf.py%20script%20in%20llama.cpp) to convert the model to gguf
5. Place the model in ```evadb_data/models```
6. See ```run_evadb.py``` for an example on how to invoke the function


## References
- Installing the EvaDB Model: https://github.com/cocktailpeanut/dalai#quickstart
- llama.cpp: https://github.com/ggerganov/llama.cpp
- llama.cpp python bindings: https://github.com/abetlen/llama-cpp-python
- EvaDB documentation: https://evadb.readthedocs.io/en/stable/index.html
- EvaDB functions: https://evadb.readthedocs.io/en/latest/source/reference/ai/custom-ai-function.html

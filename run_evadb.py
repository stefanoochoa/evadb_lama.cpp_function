# Import the EvaDB package
import evadb

# Connect to EvaDB and get a database cursor for running queries
cursor = evadb.connect().cursor()

print("Registering Function")
# Register the function
cursor.query(""" DROP FUNCTION IF EXISTS Llama """).execute()
cursor.query("""CREATE FUNCTION Llama IMPL 'evadb_data/functions/llama.py'""").execute()

print("Adding Sample Data")
# Add sample data to a table
cursor.drop_table("sample_data", if_exists=True).execute()
cursor.load("test-file.txt", "sample_data", "document").execute()

# table = cursor.query(""" SELECT * FROM sample_data """).execute()
# print(table)

print("Running Query")
#Run query and use llama function
result = cursor.table("sample_data").select(
    "Llama('summarize in detail', data)"
).df()["llama.response"]

print("printing result")
print(result[0])
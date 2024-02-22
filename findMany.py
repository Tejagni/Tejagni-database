from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://chichilitejagni:January44@cluster0.yxfoxt5.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri)

try:
    # Get reference to 'tyres' database
    db = client.tyres

    # Get reference to 'companies' collection
    companies_collection = db.companies

    # Define a query to find multiple documents
    query = {}  # This query matches all documents, you can add conditions as needed

    # Perform the find operation
    cursor = companies_collection.find(query)

    # Iterate over the cursor to access the results
    for document in cursor:
        print(document)

except Exception as e:
    print(e)
finally:
    client.close()

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint

uri = "mongodb+srv://chichilitejagni:January44@cluster0.yxfoxt5.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'tyres' database
    db = client.tyres

    # Get reference to 'companies' collection
    companies_collection = db.companies

    # Filter companies with 'industry' equal to 'Tyres'
    select_companies = {"industry": "Tyres"}

    # Update all matching documents to set 'minimum_balance' field to 100
    set_field = {"$set": {"founded_year": 1998}}
    result = companies_collection.update_many(select_companies, set_field)
    print(result)

    # Print the number of documents matched and updated
    print("Documents matched:", result.matched_count)
    print("Documents updated:", result.modified_count)

    # Printing all updated document for verification
    cursor = companies_collection.find(select_companies)

    num_docs = 0
    for document in cursor:
        num_docs += 1
        pprint.pprint(document)
        print()
    print("# of documents found: " + str(num_docs))

except Exception as e:
    print(e)
finally:
    client.close()

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

    # Filter by ObjectId
    document_to_delete = {"_id": ObjectId("65d6330ea6724bf50c81f8dd")}  # Replace ObjectId with the one you want to delete

    # Search for document before delete
    print("Searching for target document before delete: ")
    pprint.pprint(companies_collection.find_one(document_to_delete))

    # Write an expression that deletes the target company.
    result = companies_collection.delete_one(document_to_delete)

    # Search for document after delete
    print("Searching for target document after delete: ")
    pprint.pprint(companies_collection.find_one(document_to_delete))

    print("Documents deleted:", result.deleted_count)

except Exception as e:
    print(e)
finally:
    client.close()

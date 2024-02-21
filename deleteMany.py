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

    # Filter by condition (e.g., revenue less than 2000)
    documents_to_delete = {"revenue": {"$gt": 2000}}  # Adjust the condition as needed

    # Search for sample document before delete
    print("Searching for sample target document before delete: ")
    pprint.pprint(companies_collection.find_one(documents_to_delete))

    # Write an expression that deletes the target companies.
    result = companies_collection.delete_many(documents_to_delete)

    # Search for sample document after delete
    print("Searching for sample target document after delete: ")
    pprint.pprint(companies_collection.find_one(documents_to_delete))

    print("Documents deleted:", result.deleted_count)

except Exception as e:
    print(e)
finally:
    client.close()

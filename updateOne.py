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

    # Filter
    document_to_update = {"_id": ObjectId("65d6330ea6724bf50c81f8dd")}  # Replace ObjectId with the one you want to update

    # Update
    add_to_revenue = {"$inc": {"revenue": 1000000}}  # Adjust the revenue amount as needed

    # Print original document
    pprint.pprint(companies_collection.find_one(document_to_update))

    # Update the target company's revenue by the specified amount
    result = companies_collection.update_one(document_to_update, add_to_revenue)
    print("Documents updated:", result.modified_count)

    # Print updated document
    pprint.pprint(companies_collection.find_one(document_to_update))

except Exception as e:
    print(e)
finally:
    client.close()

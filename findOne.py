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

    # Get reference to 'bank' database
    db = client.bank

    # Get reference to 'accounts' collection
    accounts_collection = db.accounts

    # Document ObjectId to find
    document_to_find_id = ObjectId("65c2caeaae6140696995984e")

    # Write an expression to find the document by ObjectId
    result = accounts_collection.find_one({"_id": document_to_find_id})

    pprint.pprint(result)

except Exception as e:
    print(e)
finally:
    client.close()

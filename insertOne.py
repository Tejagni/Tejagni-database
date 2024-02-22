from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
from pprint import pprint

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

    # inserting one tyre company
    new_company = {
        "company_name": "Michelin",
        "founded_year": 1889,
        "hq_location": "Clermont-Ferrand, France",
        "industry": "Tyres",
        "revenue": 24700000000,  # Example revenue in USD for the year
        "last_updated": datetime.datetime.utcnow(),
    }

    # Write an expression that inserts the 'new_company' document into the 'companies' collection.
    result = companies_collection.insert_one(new_company)

    document_id = result.inserted_id
    pprint(f"_id of inserted document: {document_id}")

except Exception as e:
    print(e)
finally:
    client.close()

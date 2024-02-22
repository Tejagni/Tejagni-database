from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime

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

    # inserting many tyre companies
    new_companies = [
        {
            "company_name": "Bridgestone",
            "founded_year": 1931,
            "hq_location": "Kyobashi, Tokyo, Japan",
            "industry": "Tyres",
            "revenue": 33430000000,
            "last_updated": datetime.datetime.utcnow(),
        },
        {
            "company_name": "Goodyear",
            "founded_year": 1898,
            "hq_location": "Akron, Ohio, USA",
            "industry": "Tyres",
            "revenue": 15380000000,
            "last_updated": datetime.datetime.utcnow(),
        },
    ]

    # Write an expression that inserts the 'new_companies' documents into the 'companies' collection.
    result = companies_collection.insert_many(new_companies)

    document_ids = result.inserted_ids
    print("# of documents inserted: " + str(len(document_ids)))
    print(f"_ids of inserted documents: {document_ids}")

except Exception as e:
    print(e)
finally:
    client.close()

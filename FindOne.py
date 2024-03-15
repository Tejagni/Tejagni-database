from pymongo import MongoClient
from pymongo.server_api import ServerApi
import pprint


uri = "mongodb+srv://chichilitejagni:January44@cluster0.yxfoxt5.mongodb.net/"


# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


try:
   # Send a ping to confirm a successful connection
   client.admin.command('ping')


   # Get reference to 'company_management' database
   db = client.company_management


   # Get reference to 'employees' collection
   accounts_collection = db.employees


   # Perform a find one operation
   result = accounts_collection.find_one({"account_holder": "Sathvik Putta"})


   # Print the result
   pprint.pprint(result)


except Exception as e:
   print(e)
finally:
   client.close()

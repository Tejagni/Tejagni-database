from fastapi import FastAPI
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import pprint

app = FastAPI()

uri = "mongodb+srv://puttasathvik16:Sathvik123@cluster0.4xuta2y.mongodb.net/"

@app.get("/employees")
def get_employee_details():
    try:
        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))
        
        # Get reference to 'company_management' database
        db = client.company_management
        
        # Get reference to 'employees' collection
        employees_collection = db.employees
        
        # Retrieve employee details
        employee_details = list(employees_collection.find({}))
        
        return employee_details
    except Exception as e:
        return {"error": str(e)}
    finally:
        client.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

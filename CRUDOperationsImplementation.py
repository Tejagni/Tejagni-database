
import pymongo
# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://chichilitejagni:January44@cluster0.4xuta2y.mongodb.net/")
db = client["company_management"]
# Inserting an employee
employee = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "department_id": ObjectId("department_id"),
    "project_ids": [ObjectId("project_id1"), ObjectId("project_id2")]
}
result = db.employee.insert_one(employee)
print("Inserted employee ID:", result.inserted_id)

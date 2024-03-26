const { MongoClient } = require('mongodb');

// Connection URI
const uri = 'mongodb+srv://puttasathvik16:Sathvik123@cluster0.4xuta2y.mongodb.net/company_management';
const client = new MongoClient(uri);

// Function to search for employee details
async function searchEmployee(query) {
    try {
        // Connect to the MongoDB client
        await client.connect();

        // Access the company_management_system database
        const database = client.db('company_management_system');

        // Access the employee collection
        const collection = database.collection('employees');

        // Search for employee details
        const results = await collection.find({ name: { $regex: new RegExp(query, 'i') } }).toArray();
        
        return results;
    } finally {
        // Close the connection
        await client.close();
    }
}

// Example usage
async function exampleUsage() {
    const query = "John"; // Example search query
    const searchResults = await searchEmployee(query);
    console.log(searchResults);
}

exampleUsage(); // Call the example usage function

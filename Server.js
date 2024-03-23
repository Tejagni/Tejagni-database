// server.js

const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3000;

// MongoDB connection
mongoose.connect('mongodb+srv://puttasathvik16:Sathvik123@cluster0.4xuta2y.mongodb.net/', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});
const db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));

// Employee model
const Employee = mongoose.model('Employee', {
  name: String,
  id: Number,
  // Add other employee details as needed
});

// Middleware
app.use(bodyParser.json());

// Routes
app.get('/api/employees', async (req, res) => {
  try {
    const { query } = req.query;
    const employees = await Employee.find({
      $or: [
        { name: { $regex: query, $options: 'i' } },
        { id: parseInt(query) }
      ]
    });
    res.json(employees);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Start server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

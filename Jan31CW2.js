//using  sample_airbnb

//Logical operators
//and logic
db.listingsAndReviews.find({$and: [{amenities: "Washer"}, {amenities: "Dryer"}]}); 

//or logic
db.listingsAndReviews.find({$or: [{amenities: "Internet"}, {amenities: "TV"}]});

//nor
db.listingsAndReviews.find({$nor: [{amenities: "Internet"}, {amenities: "TV"}]});

//not
db.listingsAndReviews.find({$not: [{amenities: "Elevator"}]});

//andoror
db.listingsAndReviews.find({
  $and: [
    { $nor: [{ amenities: "Iron" }, { amenities: "Internet" }] },
    { $nor: [{ amenities: "Hangers" }, { amenities: "Heating" }] },
  ],
});

//elementsmatch
db.listingsAndReviews.find({amenities: {$elemMatch: {$eq: "Internet"}}});

//findArray
db.listingsAndReviews.find({amenities: "Doorman"});

//insertOne() 
db.CreateColelction("C2")
db.C2.insertOne({
  student_id: 654321,
  products: [
    {
      type: "exam",
      score: 90,
    },
    {
      type: "homework",
      score: 59,
    },
    {
      type: "quiz",
      score: 75,
    },
    {
      type: "homework",
      score: 88,
    },
  ],
  class_id: 550,
})

//Output
{
  acknowledged: true,
  insertedId: ObjectId('65bc20dfd52c2a5848ffd08b')
}

//insertMany()
db.C2.insertMany([
  {
    student_id: 546789,
    products: [
      {
        type: "quiz",
        score: 50,
      },
      {
        type: "homework",
        score: 70,
      },
      {
        type: "quiz",
        score: 66,
      },
      {
        type: "exam",
        score: 70,
      },
    ],
    class_id: 551,
  },
  {
    student_id: 777777,
    products: [
      {
        type: "exam",
        score: 83,
      },
      {
        type: "quiz",
        score: 59,
      },
      {
        type: "quiz",
        score: 72,
      },
      {
        type: "quiz",
        score: 67,
      },
    ],
    class_id: 550,
  },
  {
    student_id: 223344,
    products: [
      {
        type: "exam",
        score: 45,
      },
      {
        type: "homework",
        score: 39,
      },
      {
        type: "quiz",
        score: 40,
      },
      {
        type: "homework",
        score: 88,
      },
    ],
    class_id: 551,
  },
])

//Output
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('65bc2121d52c2a5848ffd08c'),
    '1': ObjectId('65bc2121d52c2a5848ffd08d'),
    '2': ObjectId('65bc2121d52c2a5848ffd08e')
  }

  //find
db.C2.find({ _id: ObjectId("65ba7e3507097608221bede6") })

  //greaterthan
db.C2.find({ "products.score: { $gt:70  } })

//greaterthanequalto
db.C2.find({ "products.score": { $gte: 66  } })

//lesserthan
db.C2.find({ "products.score": { $lt: 45  } })

//lesserthanequalto
db.C2.find({ "products.score": { $lte: 39  } })

  //in
db.C2.find({ student_id: { $in: [654321, 546789] } })
db.C2.find({ _id: { $in: [ObjectId('65bc2121d52c2a5848ffd08c'),  ObjectId('65bc2121d52c2a5848ffd08d')] } })

  //Mongopy
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://chichilitejagni:January44@cluster0.yxfoxt5.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    '''for db_name in client.list_database_names():
        print(db_name)*/''' #once sucessfully established connection
except Exception as e:
    print(e)

  //Output
*/ PS C:\Users\tejag> & C:/Users/tejag/AppData/Local/Microsoft/WindowsApps/python3.11.exe c:/Users/tejag/mongopy.py
Pinged your deployment. You successfully connected to MongoDB! /*




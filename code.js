db.CreateCollection("classwork")
db.classwork.insertOne({
    "Emp_ID": "10025AE336",
    "Personal_details": {
        "First_Name": "Radhika",
        "Last_Name": "Sharma",
        "Date_Of_Birth": "1995-09-26"
    },
    "Contact": {
        "e-mail": "radhika_sharma.123@gmail.com",
        "phone": "9848022338"
    },
    "Address": {
        "city": "Hyderabad",
        "Area": "Madapur",}})
//OUTPUT
/*{
  acknowledged: true,
  insertedId: 123
} */


//INSERTONE()
db.CreateCollection("sch")
db.sch.insertOne([
{
  title: "Post Title 1",
	body: "Body of post.",
	category: "News",
	likes: 1,
	tags: ["news", "events"],
	date: Date()
}
])

//OUTPUT
/* {
  acknowledged: true,
  insertedId: ObjectId('65b152e477167a4421e2b376')
} */

//INSERTMANY()
db.CreateCollection("Data")
db.Data.insertMany([
  {
    title: "Post Title 2",
    body: "Body of post.",
    category: "Event",
    likes: 2,
    tags: ["news", "events"],
    date: Date()
  },
  {
    title: "Post Title 3",
    body: "Body of post.",
    category: "Technology",
    likes: 3,
    tags: ["news", "events"],
    date: Date()
  },
  {
    title: "Post Title 4",
    body: "Body of post.",
    category: "Event",
    likes: 4,
    tags: ["news", "events"],
    date: Date()
  }
])

//OUTPUT
/* {
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('65b1545a77167a4421e2b377'),
    '1': ObjectId('65b1545a77167a4421e2b378'),
    '2': ObjectId('65b1545a77167a4421e2b379')
  }
}
*/

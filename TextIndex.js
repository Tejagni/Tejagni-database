db.student.createIndex(
  { "class_id": "hashed" },
  {
    "name": "class_id_hashed_index",
    "createdCollectionAutomatically": false,

  }
)
< class_id_hashed_index
> db.student.getIndexes() 

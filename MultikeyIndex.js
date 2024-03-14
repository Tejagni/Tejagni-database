db.student.createIndex(
  { "class_id": 1 },
  {
    "name": "class_id_multikey_index",
    "createdCollectionAutomatically": false,

  }
)
< class_id_multikey_index
> db.student.getIndexes()

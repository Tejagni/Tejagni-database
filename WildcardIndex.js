db.student.createIndex(
  { "fieldName.$**": 1 },
  { name: "wildcard_index" }
)
< wildcard_index
> db.student.getIndexes()

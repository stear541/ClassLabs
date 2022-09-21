//start mongo
start_mongo

//connect to mongodb
mongo -u root -p ***** --authenticationDatabase admin local

//Check version
db.version()

//print list of databases
show dbs

//create new database
use training

//after switching to db create collection named mycollection
db.createCollection("mycollection")

//show collections
show collections

//insert json document
db.mycollection.insert({"color":"white","example":"milk"})

//insert a lot of records
use training
for (i=1;i<=200000;i++){print(i);db.bigdata.insert({"account_no":i,"balance":Math.round(Math.random()*1000000)})}

//count number of documents in collection
db.mycollection.count()

//list all documents 
db.mycollection.find()

//list first 3 documents
db.languages.find().limit(3)

//query for string "python"
db.languages.find({"name":"python"})

//query for string "object oriented"
db.languages.find({"type":"object oriented"})

//list all docs with only the name field in the output
db.languages.find({},{"name":1})

//list all docs without name field in output
db.languages.find({},{"name":0})

//list all "object oriented" languages with only the "name" field output
db.languages.find({"type":"object oriented"},{"name":1})

//select specific account number and time to execute in milliseconds
db.bigdata.find({"account_no":58982}).explain("executionStats").executionStats.executionTimeMillis

//create index
db.bigdata.createIndex({"account_no":1})

//drop index
db.bigdata.dropIndex({"account_no":1})

//update documents based on criteria
db.collection.updateMany({what documents to find},{$set:{what fields to set}})

//add a field description with value programming language to all documents
db.languages.updateMany({},{$set:{"description":"programming language"}})

//set creator for python language document
db.languages.updateMany({"name":"python"},{$set:{"creator":"Guido van Rossum"}})

//set a field compiled with a value trye for all object oriented languages
db.languages.updateMany({"type":"object oriented"},{$set:{"compiled":true}})

//delete the scala language document
db.languages.remove({"name":"scala"})

//delete all documents in a collection
db.languages.remove({})

//aggregations
// $limit to limit number of documents printed in the output
db.marks.aggregate([{"$limit":2}])

// $sort sort the marks field in ascending order 
db.marks.aggregate([{"$sort":{"marks":1}}])

// $sort in descending order
db.marks.aggregate([{"$sort":{"marks":-1}}])

//aggregaiton pipeline with $sort and $limit here to show the top two marks 
db.marks.aggregate([
{"$sort":{"marks":-1}},
{"$limit":2}
])

//print average marks across all subjects $group by subject.  equivalent to SELECT subject, average(marks) FROM marks GROUP BY subject
db.marks.aggregate([
{
    "$group":{
        "_id":"$subject",
        "average":{"$avg":"$marks"}
        }
}
])

//find average marks per student, sort by average marks in descending order, limiting output to two documents 
db.marks.aggregate([
{
    "$group":{
        "_id":"$name",
        "average":{"$avg":"$marks"}
        }
},
{
    "$sort":{"average":-1}
},
{
    "$limit":2
}
])

//total marks for each student across all subjects
db.marks.aggregate([ { "$group":{"_id":"$name","total":{"$sum":"$marks"}} } ])

//find $max mark in each subject 
db.marks.aggregate([ { "$group":{"_id":"$subject","max_marks":{"$max":"$marks"}} } ])

//find $min mark by each student 
db.marks.aggregate([ { "$group":{"_id":"$name","min_marks":{"$min":"$marks"}} } ])

//top two subjects based on average marks
db.marks.aggregate([ { "$group":{"_id":"$subject","avg_marks":{"$avg":"$marks"}} }, {"$sort":{"avg_marks":-1}},{"$limit":2} ])

//exit mongo client 
exit 


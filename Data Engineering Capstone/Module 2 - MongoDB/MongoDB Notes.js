//Querying data in NoSQL databases

//Scenario - You are a data engineer at an e-commerce company. Your company needs you to design a data platform that uses MongoDB as a NoSQL database. You will be using MongoDB to store the e-commerce catalog data.

//Objectives
//import data into a MongoDB database.
//query data in a MongoDB database.
//export data from MongoDB.

//Tools / Software
//MongoDB Server
//MongoDB Command Line Backup Tools

//Exercise 1 - Check the lab environment
//Start MongoDB
start_mongo

//Install mongoimport and mongoexport (if needed)
wget https://fastdl.mongodb.org/tools/db/mongodb-database-tools-ubuntu1804-x86_64-100.3.1.tgz
tar -xf mongodb-database-tools-ubuntu1804-x86_64-100.3.1.tgz
export PATH=$PATH:/home/project/mongodb-database-tools-ubuntu1804-x86_64-100.3.1/bin

//JSON data - download locally 
https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/nosql/catalog.json

//Exercise 2 - Working with MongoDB (linux shell)
//Task 1 - Import json file into MongoDB server into a database named catalog an a collection named electronics
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/nosql/catalog.json
mongoimport -u root -p **hidden** --authenticationDatabase admin --db catalog --collection electronics --file catalog.json

//screenshot mongoimport.PNG 

//Task 2 - List out all of the databases (mongodb shell)
show dbs

//screenshot list-dbs.PNG 

//Task 3 - List out all collections in the catalog database
use catalog
show collections 

//screenshot list-collections.PNG

//Task 4 - Create an index on the field "type"
db.electronics.createIndex({"type":1})

//screenshot create-index.PNG 

//Task 5 - Write a query to find the count of laptops
db.electronics.count({"type":"laptop"})

//screenshot mongo-query-laptops.PNG

//Task 6 - Write query to find number of smart phones with a screen size of 6 inches
db.electronics.count({"type":"smart phone"}, {"screen size":"6"})

//screenshot mongo-query-mobiles1.PNG 

//Task 7 - Query to find average screen size of documents grouped by type 
db.electronics.aggregate([{"$group":{"_id":"$type","average":{"$avg":"$screen size"}}}])

//screenshot mongo-query-mobiles2.PNG 

//Task 8 - Export the fields _id, type, and model from the electonics collection into a file named electronics.csv
//in linux shell 
mongoexport -u root -p **hidden** --authenticationDatabase admin --db catalog --collection electronics --out electronics.csv --type=csv --fields _id,type,model

//screenshot mongoexport.PNG 

//quit mongo
exit 


























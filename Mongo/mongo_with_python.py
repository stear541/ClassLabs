#install the pymongo driver n the linux cli
# pip install pymongo 

#start the server
# start_mongo

#create new file in the menu, named mongo_connect.py

#copy and paste the script into the file 
from pymongo import MongoClient
user = 'root'
password = '*****'
host='localhost'

#create the connection url
connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user,password,host)


# connect to mongodb server
print("Connecting to mongodb server")
connection = MongoClient(connecturl)


# get database list
print("Getting list of databases")
dbs = connection.list_database_names()

# print the database names

for db in dbs:
    print(db)
print("Closing the connection to the mongodb server")


# close the server connecton
connection.close()

#now run the script in CLI
# python3 mongo_connect.py

#create a new file ccalled mongo_qury.py and paste the following
from pymongo import MongoClient
user = 'root'
password = '*****'
host='localhost'
#create the connection url
connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user,password,host)

# connect to mongodb server
print("Connecting to mongodb server")
connection = MongoClient(connecturl)

# select the 'training' database 

db = connection.training

# select the 'python' collection 

collection = db.python

# create a sample document

doc = {"lab":"Accessing mongodb using python", "Subject":"No SQL Databases"}

# insert a sample document

print("Inserting a document into collection.")
db.collection.insert_one(doc)

# query for all documents in 'training' database and 'python' collection

docs = db.collection.find()

print("Printing the documents in the collection.")

for document in docs:
    print(document)

# close the server connecton
print("Closing the connection.")
connection.close()





# Practice python script
#connect to the mongodb server.
#select a database named training.
#select a collection named mongodb_glossary.
#insert the following documents into the collection mongodb_glossary.
	#{“database”:”a database contains collections”}
	#{“collection”:”a collection stores the documents”}
	#{“document”:”a document contains the data in the form of key value pairs.”}
#query and print all the documents in the training database and mongodb_glossary collection.
#close the connection to the server.

from pymongo import MongoClient
user = 'root'
password = '*****'
host='localhost'
#create the connection url
connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user,password,host)

# connect to mongodb server
print("Connecting to mongodb server")
connection = MongoClient(connecturl)

# select the 'training' database 

db = connection.training

# select the 'python' collection 

collection = db.mongodb_glossary

# create documents

doc1 = {"database":"a database contains collections"}
doc2 = {"collection":"a collection stores the documents"}
doc3 = {"document":"a document contains the data in the form or key value pairs."}

# insert documents
print("Inserting documents into collection.")

db.collection.insert_one(doc1)
db.collection.insert_one(doc2)
db.collection.insert_one(doc3)

# query for all documents in 'training' database and 'python' collection

docs = db.collection.find()

print("Printing the documents in the collection.")

for document in docs:
    print(document)

# close the server connecton
print("Closing the connection.")
connection.close()
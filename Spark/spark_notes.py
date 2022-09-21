# Installing required packages
!pip install pyspark
!pip install findspark

import findspark
findspark.init()

# PySpark is the Spark API for Python. In this lab, we use PySpark to initialize the spark context. 
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

# Creating a spark context class
sc = SparkContext()

# Creating a spark session
spark = SparkSession \
    .builder \
    .appName("Python Spark DataFrames basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
	
#verify that the spark session instance has been created
spark

#create RDD which has ints 1 to 30
data = range(1,30)
# print first element of iterator
print(data[0])
len(data)
xrangeRDD = sc.parallelize(data, 4)  #the 4 represents 4 partitions 

# this will let us know that we created an RDD
xrangeRDD

#transformation, reduce each element in og RDd by 1.  Then another filter on the og RDD to only contain elements < 10.
subRDD = xrangeRDD.map(lambda x: x-1)
filteredRDD = subRDD.filter(lambda x : x<10)

#apply collect action to get the output from the transformation
print(filteredRDD.collect())
filteredRDD.count()

#caching data.  create an RDD and cache it.  notice the 10x speed improvement.
import time 

test = sc.parallelize(range(1,50000),4)
test.cache()

t1 = time.time()
# first count will trigger evaluation of count *and* cache
count1 = test.count()
dt1 = time.time() - t1
print("dt1: ", dt1)


t2 = time.time()
# second count operates on cached data only
count2 = test.count()
dt2 = time.time() - t2
print("dt2: ", dt2)

#test.count()


#Create a dataframe!!
# Download the data first into a local `people.json` file
!curl https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0225EN-SkillsNetwork/labs/data/people.json >> people.json

# Read the dataset into a spark dataframe using the `read.json()` function
df = spark.read.json("people.json").cache()

# Print the dataframe as well as the data schema
df.show()
df.printSchema()

# Register the DataFrame as a SQL temporary view
df.createTempView("people")

# Select and show basic data columns
df.select("name").show()
df.select(df["name"]).show()
spark.sql("SELECT name FROM people").show()

# Perform basic filtering
df.filter(df["age"] > 21).show()
spark.sql("SELECT age, name FROM people WHERE age > 21").show()

# Perfom basic aggregation of data
df.groupBy("age").count().show()
spark.sql("SELECT age, COUNT(age) as count FROM people GROUP BY age").show()


#example 1 - create RDD with ints from 1 to 50.  Apply transformation to multiply every number by 2.
numbers = range(1, 50)
numbers_RDD = sc.parallelize(numbers, 4)
even_numbers_RDD = numbers_RDD.map(lambda x: x*2)
print(even_numbers_RDD.collect())

#example 2 - new data, find average age
# Code block for learners to answer
!curl https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0225EN-SkillsNetwork/labs/people2.json >> people2.json
df = spark.read.json("people2.json").cache()
df.createTempView("people2")
spark.sql("SELECT AVG(age) from people2").show()

#close the SparkSession
spark.stop()
#intro to dataframes with python / spark
# Installing required packages
!pip install pyspark
!pip install findspark
!pip install pandas

import findspark
findspark.init()

import pandas as pd
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

#create the spark session and context
# Creating a spark context class
sc = SparkContext()

# Creating a spark session
spark = SparkSession \
    .builder \
    .appName("Python Spark DataFrames basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
	
#verify the spark session instance has been created
spark

#read a csv into pandas dataframe and then into a spark dataframe
# Read the file using `read_csv` function in pandas
mtcars = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0225EN-SkillsNetwork/labs/data/mtcars.csv')

# Preview a few records
mtcars.head()

# We use the `createDataFrame` function to load the data into a spark dataframe
sdf = spark.createDataFrame(mtcars) 

# Let us look at the schema of the loaded spark dataframe
sdf.printSchema()

#show first 5 records with spark.  similar to pandas head
sdf.show(5)

#select to show a specific columnn of data
sdf.select('mpg').show(5)

#filter records
sdf.filter(sdf['mpg'] < 18).show(5)
sdf.filter(sdf['cyl'] > 4).show(5)

#convert weight from pounds to metric tons into a new column called wtTon
sdf.withColumn('wtTon', sdf['wt'] * 0.45).show(5)

#mean weight of cars in metric tons
sdf.withColumn('wtTon', sdf['wt'] * 0.45).agg({'wtTon':"AVG"}).show()

#compute the average weight of cars by their cylinders
sdf.groupby(['cyl']).agg({"wt": "AVG"}).show(5)


#sort output from the aggregation to get the most common cars
car_counts = sdf.groupby(['cyl'])\
.agg({"wt": "count"})\
.sort("count(wt)", ascending=False)\
.show(5)

#new column to convert mpg to kilometers per liter, sort descending
sdf.withColumn('kmpl', sdf['mpg'] * 0.425).sort("kmpl", ascending=False).show(5)


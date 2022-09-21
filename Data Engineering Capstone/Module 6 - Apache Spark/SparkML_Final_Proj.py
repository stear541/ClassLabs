#install spark
!pip install pyspark
!pip install findspark

#Import Libraries
import findspark
findspark.init()
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

# Start session
#Create Spark context class
sc = SparkContext()
#Create spark session
spark = SparkSession.builder.appName("Saving and Loading a SparkML Model").getOrCreate()

spark

#import SparkML libraries
from pyspark.ml.feature import VectorAssembler, Normalizer, StandardScaler
from pyspark.ml.stat import Correlation
from pyspark.ml.regression import LinearRegression

# Download The search term dataset from the below url
# https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/Bigdata%20and%20Spark/searchterms.csv
import pandas as pd
searchterms = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/Bigdata%20and%20Spark/searchterms.csv')
searchterms.head()

# Load the csv into a spark dataframe
sdf = spark.createDataFrame(searchterms)
sdf.printSchema()

# Print the number of rows and columns
# Take a screenshot of the code and name it as shape.jpg)
rows = sdf.count()
col = len(sdf.columns)

print(f'Number of Rows are: {rows}')
print(f'Number of Columns are: {col}')

# Print the top 5 rows
# Take a screenshot of the code and name it as top5rows.jpg)
sdf.show(5)

# Find out the datatype of the column searchterm?
# Take a screenshot of the code and name it as datatype.jpg)
sdf.printSchema()

# How many times was the term `gaming laptop` searched?
# Take a screenshot of the code and name it as gaminglaptop.jpg)
sdf.createOrReplaceTempView("searchterms")
query1 = spark.sql("SELECT count(*) from searchterms where searchterm = 'gaming laptop'")
query1.show()

# Print the top 5 most frequently used search terms?
# Take a screenshot of the code and name it as top5terms.jpg)
query2 = spark.sql("SELECT distinct searchterm, count(*) as count from searchterms group by searchterm order by count desc limit 5")
query2.show()

# The pretrained sales forecasting model is available at  the below url
# https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/Bigdata%20and%20Spark/model.tar.gz
import tarfile
import urllib.request

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/Bigdata%20and%20Spark/model.tar.gz'
filename = 'model.tar.gz'
urllib.request.urlretrieve(url, filename)

#open file
file = tarfile.open(filename)

#extract file
file.extractall('./')

# Load the sales forecast model.
# Take a screenshot of the code and name it as loadmodel.jpg)
from pyspark.ml.regression import LinearRegressionModel

model = LinearRegressionModel.load('sales_prediction.model')

# Using the sales forecast model, predict the sales for the year of 2023.
# Take a screenshot of the code and name it as forecast.jpg
def predict(year):
    assembler = VectorAssembler(inputCols=["year"],outputCol="features")
    data = [[year,0]]
    columns = ["year", "sales"]
    _ = spark.createDataFrame(data, columns)
    __ = assembler.transform(_).select('features','sales')
    predictions = model.transform(__)
    predictions.select('prediction').show()

predict(2023)
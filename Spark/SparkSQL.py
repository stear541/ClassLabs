#SparkSQL

# Installing required packages
!pip install pyspark
!pip install findspark
!pip install pyarrow==1.0.0
!pip install pandas
!pip install numpy==1.19.5

import findspark
findspark.init()

import pandas as pd
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

#create spark session and context
# Creating a spark context class
sc = SparkContext()

# Creating a spark session
spark = SparkSession \
    .builder \
    .appName("Python Spark DataFrames basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
	
#verify session
spark

#load data into pandas df
# Read the file using `read_csv` function in pandas
mtcars = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0225EN-SkillsNetwork/labs/data/mtcars.csv')

# Preview a few records
mtcars.head()

#rename the first column
mtcars.rename( columns={'Unnamed: 0':'name'}, inplace=True )

#create spark dataframe with function 
sdf = spark.createDataFrame(mtcars) 

#check schema
sdf.printSchema()

#create temporary view.  required for spark SQL queries
sdf.createTempView("cars")

# Showing the whole table
spark.sql("SELECT * FROM cars").show()

# Showing a specific column
spark.sql("SELECT mpg FROM cars").show(5)

# Basic filtering query to determine cars that have a high mileage and low cylinder count
spark.sql("SELECT * FROM cars where mpg>20 AND cyl < 6").show(5)

#show them Mercedez Benz
spark.sql("select * from cars where name like 'Merc%'").show()

# Aggregating data and grouping by cylinders
spark.sql("SELECT count(*), cyl from cars GROUP BY cyl").show()


#create Scalar Pandas user-defined function.  Convert wT column from imperial units to metric units 

# import the Pandas UDF function 
from pyspark.sql.functions import pandas_udf, PandasUDFType

@pandas_udf("float")
def convert_wt(s: pd.Series) -> pd.Series:
    # The formula for converting from imperial to metric tons
    return s * 0.45

spark.udf.register("convert_weight", convert_wt)

#apply the UDF to the table view
spark.sql("SELECT *, wt AS weight_imperial, convert_weight(wt) as weight_metric FROM cars").show()

#new UDF to convert mpg to kmpl
@pandas_udf("float")
def convert_mileage(s: pd.Series) -> pd.Series:
    # The formula for converting from imperial to metric tons
    return s * 0.425

spark.udf.register("convert_mileage", convert_mileage)

spark.sql("SELECT *, mpg AS mpg, convert_weight(mpg) as kmpl FROM cars").show()









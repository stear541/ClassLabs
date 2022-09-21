#Hands on Lab - Saving and Loading SparkML model

#Objectives:  Create simple Linear Regression Model, Save the SparkML model, Load the SparkML model, Make predictions using the loaded SparkML model

#Install PySpark
!pip install pyspark
!pip install findspark

#Import Libraries
import findspark
findspark.init()
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

#Create Spark context class
sc = SparkContext()
#Create spark session
spark = SparkSession.builder.appName("Saving and Loading a SparkML Model").getOrCreate()

#import SparkML libraries
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression

#Create a DataFrame with sample data - infant height(cm) and weight(kgs) chart
mydata = [[46,2.5],[51,3.4],[54,4.4],[57,5.1],[60,5.6],[61,6.1],[63,6.4]]
#column names of dataframe
columns = ["height","weight"]
#create dataframe
mydf = spark.createDataFrame(mydata, columns)
#show the dataframe
mydf.show()

#Convert dataframe columns into feature vectors using VectorAssembler() function.  
assembler = VectorAssembler(
    inputCols=["height"],
    outputCol="features")
data = assembler.transform(mydf).select('features','weight')

data.show()

#Create model using LinearRegression() class and Train using fit() function
# Create a LR model
lr = LinearRegression(featuresCol='features', labelCol='weight', maxIter=100)
lr.setRegParam(0.1)
# Fit the model
lrModel = lr.fit(data)

#Save the model
lrModel.save('infantheight2.model')

#Load the model using LinearRegressionModel
from pyspark.ml.regression import LinearRegressionModel

model = LinearRegressionModel.load('infantheight2.model')

#Make Prediction - Predict the weight of an infant whose height is 70 cms
# This function converts a scalar number into a dataframe that can be used by the model to predict.
def predict(weight):
    assembler = VectorAssembler(inputCols=["weight"],outputCol="features")
    data = [[weight,0]]
    columns = ["weight", "height"]
    _ = spark.createDataFrame(data, columns)
    __ = assembler.transform(_).select('features','height')
    predictions = model.transform(__)
    predictions.select('prediction').show()

#run the prediction 
predict(70)


#Practice Exercises
#save the model as babyweightprediction.model
lrModel.save('babyweightprediction.model')

#Load the model babyweightprediction
model = LinearRegressionModel.load('babyweightprediction.model')

#Predict the weight of infant whose height is 50cm
predict(50)


















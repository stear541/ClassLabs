# When you are executing on SN labs please uncomment the below lines and then run all cells.Next again Restart the kernel and run all cells.
!pip3 install pyspark==3.1.2
!pip install findspark
import findspark
findspark.init()

# Pandas is a popular data science package for Python. In this lab, we use Pandas to load a CSV file from disc to a pandas dataframe in memory.
import pandas as pd
import matplotlib.pyplot as plt
# pyspark is the Spark API for Python. In this lab, we use pyspark to initialize the spark context. 
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

#Initialize Spark session
spark

#import Spark ML libraries
from pyspark.ml.feature import VectorAssembler, Normalizer, StandardScaler
from pyspark.ml.stat import Correlation
from pyspark.ml.regression import LinearRegression

# Read the file using `read_csv` function in pandas
cars = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0225EN-SkillsNetwork/labs/data/cars.csv')

# Preview a few records
cars.head()

#we only need the pre-processed data in this lab
cars2 = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0225EN-SkillsNetwork/labs/data/cars2.csv', header=None, names=["mpg", "hp", "weight"])
cars2.head()

# We use the `createDataFrame` function to load the data into a spark dataframe
sdf = spark.createDataFrame(cars2)

# Let us look at the schema of the loaded spark dataframe
sdf.printSchema()

#Next use VectorAssembler() function to convert dataframe columns into feature vectors.  For this example use hp and weight of cars as input features and mpg as target labels
assembler = VectorAssembler(
    inputCols=["hp", "weight"],
    outputCol="features")

output = assembler.transform(sdf).select('features','mpg')

#we now create a test-train split of 75%-25%
train, test = output.randomSplit([0.75, 0.25])

#Now determine correlation between feature vectors and normalize the features
#Spark ML has inbuilt Correlation function as part of the Stat library. 
#Use correlation function to determine different types of correlation between the 2 features, hp and weight

r1 = Correlation.corr(train, "features").head()
print("Pearson correlation matrix:\n" + str(r1[0]))

#output: Pearson correlation matrix: DenseMatrix([[1., 0.85638102], [0.85638102, 1.]])

r2 = Correlation.corr(train, "features", "spearman").head()
print("Spearman correlation matrix:\n" + str(r2[0]))

#output:  Spearman correlation matrix: DenseMatrix([[1., 0.86891998], [0.86891998, 1.]])

#We can see that there is a 0.86 (or 86%) correlation between the features. That is logical as a car with higher horsepower likely has a bigger engine and thus weighs more. We can also visualize the feature vectors to see that they are indeed correlated.

plt.figure()
plt.scatter(cars2["hp"], cars2["weight"])
plt.xlabel("horsepower")
plt.ylabel("weight")
plt.title("Correlation between Horsepower and Weight")
plt.show()

#Normalization
#In order for better model training and convergence, it is a good practice to normalize feature vectors.

normalizer = Normalizer(inputCol="features", outputCol="features_normalized", p=1.0)
train_norm = normalizer.transform(train)
print("Normalized using L^1 norm")
train_norm.show(5, truncate=False)

#output 
#Normalized using L^1 norm
+-------------+----+-----------------------------------------+
|features     |mpg |features_normalized                      |
+-------------+----+-----------------------------------------+
|[46.0,1835.0]|26.0|[0.024455077086656035,0.9755449229133439]|
|[49.0,1867.0]|29.0|[0.0255741127348643,0.9744258872651357]  |
|[52.0,1649.0]|31.0|[0.030570252792475015,0.969429747207525] |
|[52.0,2035.0]|29.0|[0.024916147580258743,0.9750838524197413]|
|[53.0,1795.0]|33.0|[0.02867965367965368,0.9713203463203464] |
+-------------+----+-----------------------------------------+

#Standard Scaling
#This is a standard practice to scale the features such that all columns in the features have zero mean and unit variance.
standard_scaler = StandardScaler(inputCol="features", outputCol="features_scaled")
train_model = standard_scaler.fit(train)
train_scaled = train_model.transform(train)
train_scaled.show(5, truncate=False)

#output
+-------------+----+---------------------------------------+
|features     |mpg |features_scaled                        |
+-------------+----+---------------------------------------+
|[46.0,1835.0]|26.0|[1.2019771153661571,2.1612219561323323]|
|[49.0,1867.0]|29.0|[1.280366927237863,2.1989108403809614] |
|[52.0,1649.0]|31.0|[1.358756739109569,1.9421553164371748] |
|[52.0,2035.0]|29.0|[1.358756739109569,2.396777482686265]  |
|[53.0,1795.0]|33.0|[1.3848866764001375,2.114110850821546] |
+-------------+----+---------------------------------------+

test_scaled = train_model.transform(test)
test_scaled.show(5, truncate=False)

#output
+-------------+----+---------------------------------------+
|features     |mpg |features_scaled                        |
+-------------+----+---------------------------------------+
|[46.0,1950.0]|26.0|[1.2019771153661571,2.2966663839008437]|
|[60.0,1834.0]|27.0|[1.5677962374341181,2.1600441784995628]|
|[61.0,2003.0]|32.0|[1.5939261747246867,2.3590885984376357]|
|[70.0,1937.0]|29.0|[1.8290956103398044,2.281355274674838] |
|[70.0,1955.0]|26.0|[1.8290956103398044,2.302555272064692] |
+-------------+----+---------------------------------------+

#Building and Training a Linear Regression Model
#Train a Linear Regression model lrModel on our training dataset. We train the model on the standard scaled version of features. Also print the final RMSE and R-Squared metrics.
#Create the model using  LinearRegression() class and train using the fit() function
# Create a LR model
lr = LinearRegression(featuresCol='features_scaled', labelCol='mpg', maxIter=100)

# Fit the model
lrModel = lr.fit(train_scaled)

# Print the coefficients and intercept for linear regression
print("Coefficients: %s" % str(lrModel.coefficients))
print("Intercept: %s" % str(lrModel.intercept))

# Summarize the model over the training set and print out some metrics
trainingSummary = lrModel.summary
#trainingSummary.residuals.show()
print("RMSE: %f" % trainingSummary.rootMeanSquaredError)
print("R-squared: %f" % trainingSummary.r2)

#output: 
Coefficients: [-1.8821305240091624,-5.046876663287883]
Intercept: 46.31948854552632
RMSE: 4.292294
R-squared: 0.710089
#We see a RMSE (Root mean squared error) of 4.26. This means that our model predicts the mpg with an average error of 4.2 units.

#Predict on new data
#Once a model is trained, we can then transform() new unseen data (for eg. the test data) to generate predictions. In the below cell, notice the "prediction" column that contains the predicted "mpg".
lrModel.transform(test_scaled).show(5)

#output:
+-------------+----+--------------------+------------------+
|     features| mpg|     features_scaled|        prediction|
+-------------+----+--------------------+------------------+
|[46.0,1950.0]|26.0|[1.20197711536615...| 32.46621875126826|
|[60.0,1834.0]|27.0|[1.56779623743411...|32.467214835484555|
|[61.0,2003.0]|32.0|[1.59392617472468...|  31.4134822449764|
|[70.0,1937.0]|29.0|[1.82909561033980...|31.363173169549444|
|[70.0,1955.0]|26.0|[1.82909561033980...|31.256179397460826|
+-------------+----+--------------------+------------------+

#Lab Questions
#Print the correlation matrix for the test dataset split we created above
r1 = Correlation.corr(test, "features").head()
print("Pearson correlation matrix:\n" + str(r1[0]))

#Normalize the training features by using the L2 norm of the feature vector
normalizer_l2 = Normalizer(inputCol="features", outputCol="features_normalized", p=2.0)
train_norm_l2 = normalizer_l2.transform(train)
print("Normalized using L^1 norm\n"+str(train_norm_l2))
train_norm_l2.show(5, truncate=False)

#Train the model.  Repeat the training model shown above for another 100 iterations and report the coefficients

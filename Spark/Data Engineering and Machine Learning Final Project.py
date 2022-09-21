#Task 1: Import the component library. (1 pt)
#Task 2: Explore component library transformations. (1 pt)
#Task 3: Convert .csv to Parquet. (1 pt)
#Task 4: Perform model training. (1 pt)
#Task 5: Complete the model training. (1 pt)
#Task 6: Deploy the model to Watson Machine Learning. (1 pt)
#Task 7: Perform model inference. (2 pts) 
#Task 8: HyperParameter Tuning. (3 pts)
highestAccuracy = 0
bestConfiguration = None

for maxIter in [10, 100, 1000]:
	for regParam in [0.01, 0.5, 2.0]:
		for elasticNetParam in [0.0, 0.5, 1.0]:
			lr = LogisticRegression(maxIter=maxIter, regParam=regParam, elasticNetParam = elasticNetParam)
			pipeline = Pipeline(stages=[indexer, vectorAssembler, normalizer, lr])
			model = pipeline.fit(df_train)
			prediction = model.transform(df_train)
			binEval = MulticlassClassificationEvaluator().setMetricName("accuracy").setPredictionCol("prediction").setLabelCol("label")
			accuracy = bin.Eval.evaluate(prediction)
			output = f"maxIter: {maxIter:4.0f}, regParam: {regParam:3.0f}, elasticNetParam: {elasticNetParam:1.1f} => accuracy: {accuracy}"
			if accuracy > highestAccuracy:
			highestAccuracy = accuracy
			bestConfiguration = output
			
			print(output)

"Best configuration was", bestConfiguration


#Task 9: Resample data splits. (3 pts) 
pipeline = Pipeline(stages=[indexer, vectorAssembler, normalizer, lr])


def run_training(weights, seed=1):  #random seed of 1
	splits = df.randomSplit(weights, seed=seed)
	df_train = splits[0]
	df_test = splits[1]
	
	model = pipeline.fit(df_train)
	prediction = model.transform(df_train)
	
	bin_eval = MulticlassClassificationEvaluator().setMetricName("accuracy").setPredictionCol("prediction").setLabelCol("label")
	
	accuracy = binEval.evaluate(prediction)
	
	print(weights, accuracy)
	
run_training(weights=[0.7, 0.3])  #70:30 train:test split

run_training(weights=[0.9, 0.1]) #90:10 train:test split


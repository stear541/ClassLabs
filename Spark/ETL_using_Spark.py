#CLAIMED repo is open-source library of notebooks (Component Library for AI, Machine Learning, ETL, and Data Science)
#https://github.com/IBM/claimed/tree/master/component-library

#download CLAIMED library from github, takes a few mins 
%%bash
rm -Rf claimed
git clone https://github.com/*****
cd claimed

#navigate to claimed/component-library/transform/spark-csv-to-parquet.ipynb

#pull the data from claimed/component-library/input/input-hmp.ipynb
#run each cell top down, or run the following to bulk run the notebook
!ipython ./claimed/component-library/input/input-hmp.ipynb data_dir=./data/ sample=0.01


#now convert from csv to parquet
!ipython ./claimed/component-library/transform/spark-csv-to-parquet.ipynb data_dir=./data/

#condense the parquet file
!ipython ./claimed/component-library/transform/spark-condense-parquet.ipynb data_dir=./data/

#deploy file to cloud object storage 
%%bash
export access_key_id='*****'
export secret_access_key='*****'
export endpoint='endpoint=https://*****'
export bucket_name='*****'
export source_file='source_file=data_condensed.parquet'
export destination_file='destination_file=data.parquet'
export data_dir='data_dir=./data/'
ipython ./claimed/component-library/output/upload-to-cos.ipynb $access_key_id $secret_access_key $endpoint $bucket_name $source_file $destination_file $data_dir
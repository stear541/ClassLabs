#Scenario
#Write a pipeline that analyzes the web server log file, extracts the required lines(ending with html) and fields(time stamp, size ) and transforms (bytes to mb) and load (append to an existing file.)

#Objectives: In this assignment you will author an Apache Airflow DAG that will:
#Extract data from a web server log file
#Transform the data
#Load the transformed data into a tar file

#Tools/Software:  Apache Airflow 

#Exercise 1 - Prepare the lab environment
#Before you start the assignment:
#Start Apache Airflow.
#Download the dataset from the source to the destination /home/project/airflow/dags/capstone
cd airflow/dags/
sudo mkdir capstone
cd capstone
sudo wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/accesslog.txt

#Exercise 2 - Crate a DAG
#Task 1 - Define the DAG Arguments.  Create a Dag with the following arguments:  owner, start_date, email.  You may define any suitable additional arguments.  dag_args.PNG
sudo touch capstone_dag.py

#import the libraries
from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago

#defining DAG arguments
default_args = {
    'owner': 'Michael Jordan',
    'start_date': days_ago(0),
    'email': ['mj23@somemail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

#Task 2 - Define the DAg.   Create a DAG named process_web_log with suitable description.
# define the DAG
dag = DAG(
    'process_web_log',
    default_args=default_args,
    description='Process Web Log Daily',
    schedule_interval=timedelta(days=1),
)

#Task 3 - Create a task to extract data.  This task should extract the ipaddress field from the web server log file and save it into a file named extracted_data.txt.  screenshot extract_data.PNG
extract_data = BashOperator(
    task_id='extract_data',
    bash_command='cut -d"-" -f 1 /home/project/airflow/dags/capstone/accesslog.txt > /home/project/airflow/dags/capstone/extracted_data.txt',
    dag=dag,
)

#Task 4 - Task to filter the ipaddress 198.46.149.143.  screenshot transformed_data.PNG 
transform_data = BashOperator(
    task_id='transform_data',
    bash_command='grep -v "$198.46.149.143" /home/project/airflow/dags/capstone/extracted_data.txt > /home/project/airflow/dags/capstone/transformed_data.txt',
    dag=dag
)

#Task 5 - Load the data - archive to weblog.tar.  screenshot load_data.PNG 
load_data = BashOperator(
    task_id='load_data',
    bash_command='tar -zcvf /home/project/airflow/dags/capstone/weblog.tar.gz /home/project/airflow/dags/capstone/transformed_data.txt',
    dag=dag
)


# task pipeline with screenshot pipeline.PNG 
extract_data >> transform_data >> load_data

#finally submit the dag
#   cp process_web_log.py $AIRFLOW_HOME/dags
#submit_dag.PNG 

#unpause the dag and screenshot unpause_dag.PNG
#  airflow dags unpause process_web_log 

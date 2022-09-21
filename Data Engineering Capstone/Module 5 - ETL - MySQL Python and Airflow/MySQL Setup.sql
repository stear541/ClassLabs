--Scenario
--You are a data engineer at an e-commerce company. You need to keep data synchronized between different databases/data warehouses as a part of your daily routine. One task that is routinely performed is the sync up of staging data warehouse and production data warehouse. Automating this sync up will save you a lot of time and standardize your process. You will be given a set of python scripts to start with. You will use/modify them to perform the incremental data load from MySQL server which acts as a staging warehouse to the IBM DB2 which is a production data warehouse. This script will be scheduled by the data engineers to sync up the data between the staging and production data warehouse.

--Objectives:  In this assignment you will write a python program that will:
--Connect to IBM DB2 data warehouse and identify the last row on it.
--Connect to MySQL staging data warehouse and find all rows later than the last row on the datawarehouse.
--Insert the new data in the MySQL staging data warehouse into the IBM DB2 production data warehouse.

--Tools / Software: MySQL Server, IBM DB2 database running on IBM Cloud

--Prepare the lab environment.  Before you start the assignment:
--Step 1: Start MySQL server
--Step 2: Create a database named sales
create database sales;
--Step 3: Download the file:  https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/sales.sql
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/sales.sql
--Step 4: Import the data in the file sales.sql into the sales database.
use sales;
source sales.sql;
--Step 5: Verify that you can access your cloud instance of IBM DB2 server.
--Step 6: Download the mysqlconnect.py python programs from:  https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/mysqlconnect.py
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/mysqlconnect.py
--Step 7: mysqlconnect.py has the sample code to help you understand how to connect to MySQL using Python.
--Step 8: Modify mysqlconnect.py suitably and make sure you are able to connect to the MySQL server instance on the Theia environment.
--Change password
pip3 install mysql-connector-python
python3 mysqlconnect.py
--Step 9: Download the db2connect.py python programs from:  https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/db2connect.py
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/db2connect.py
--Step 10: db2connect.py has the sample code to help you understand how to connect to the cloud instance of IBM DB2 using Python.
--Step 11: Modify db2connect.py suitably and make sure you are able to connect to your cloud instance of IBM DB2 from the Theia environment.
--Check service credentials
pip3 install ibm-db
python3 db2connect.py
--Step 12: Download the file:  https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/sales.csv
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/sales.csv
--Step 13: Load sales.csv into a table named sales_data on your cloud instance of IBM DB2 database.
--Step 14: https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/automation.py
--You will be using automation.py as a scafolding program to execute the tasks in this assignment
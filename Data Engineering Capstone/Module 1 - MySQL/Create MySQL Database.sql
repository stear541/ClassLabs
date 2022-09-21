--Exercise 1 - Check the lab environment
--Start MySQL server

--Exercise 2 - Design the OLTP Database 
--Task 1 - Create a database names sales
CREATE DATABASE sales;
use sales;

--Task 2 - Design a table names sales_data.  Columns include product_id, customer_id, price, quantity, timestamp
DROP TABLE IF EXISTS sales_data;
CREATE TABLE sales_data(
product_id INTEGER NOT NULL,
customer_id INTEGER NOT NULL,
price DECIMAL(12, 2),
quantity INTEGER,
timestamp timestamp);

--screenshot createtable.PNG 

--Exercise 3 - Load the database
--Task 3 - Import the data in the file oltpdata.csv
--Download the csv data locally from here:   https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/oltp/oltpdata.csv
--Import the data using phpMyAdmin
--Take a screenshot of import status importdata.PNG

--Task 4 - List the tables in the database sales
use sales;
show tables;
--screenshot query and output listtables.PNG

--Task 5 - Write query to find the count of records in the sales_data table
select count(*) from sales_data;
--screenshot salesrows.PNG

--Exercise 4 - Setup admin tasks
--Task 6 - Create an index named ts on the timestamp field
CREATE INDEX ts on sales_data(timestamp);

--Task 7 - List INDEXES
show index from sales.sales_data;
--screenshot listindexes.PNG

--Task 8 - Write a Bash script to export data from sales_data to a file named salesdata.sql
mkdir module1_mysql
cd module1_mysql

#!/bin/bash

echo "Enter username:"
read u
echo "Enter Password:"
read p
mysql --host=127.0.0.1 --port=3306 --user=${u} --password=${p}     \
mysqldump sales.sales_data > salesdata.sql


bash datadump.sh

--screenshot of .sh and output exportdata.PNG
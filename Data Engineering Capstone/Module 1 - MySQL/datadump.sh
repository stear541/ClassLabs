#!/bin/bash

echo "Enter username:"
read u
echo "Enter Password:"
read p
mysql --host=127.0.0.1 --port=3306 --user=${u} --password=${p}     \
mysqldump sales.sales_data > salesdata.sql
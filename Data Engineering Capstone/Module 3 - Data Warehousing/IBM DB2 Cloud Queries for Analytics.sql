--Load csv data into IBM DB2 on Cloud

--Exercise 2 - Queries for Analytics
--Task 5 - Create a grouping sets query
--Create a grouping sets query using the columns country, category, totalsales.
--Screenshot goupingsets.PNG
select country, category,
sum(amount) as totalsales
from softcartFactSales
left join softcartDimCountry
on softcartFactSales.countryid = softcartDimCountry.countryid
left join softcartDimCategory
on softcartFactSales.categoryid = softcartDimCategory.categoryid
group by grouping sets(country, category, amount)
order by country, category, amount;

--Task 6 - Create a rollup query
--Create a rollup query using the columns year, country, and totalsales.
--rollup.PNG
select year, country, sum(amount) as totalsales
from softcartFactSales
left join softcartDimCountry
on softcartFactSales.countryid = softcartDimCountry.countryid
left join softcartDimDate
on softcartFactSales.dateid = softcartDimDate.dateid
group by rollup(year, country, amount);

--Task 7 - Create a cube query
--Create a cube query using the columns year, country, and average sales.
--cube.PNG
select year, country, avg(amount) as avg_sales
from softcartFactSales
left join softcartDimCountry
on softcartFactSales.countryid = softcartDimCountry.countryid
left join softcartDimDate
on softcartFactSales.dateid = softcartDimDate.dateid
group by cube(year, country, amount);

--Task 8 - Create an MQT
--Create an MQT named total_sales_per_country that has the columns country and total_sales.
--mqt.PNG
DROP TABLE IF EXISTS total_sales_per_country;
CREATE TABLE total_sales_per_country 
(country, totalsales) 
AS
    (select country, sum(amount) as totalsales
    from softcartFactSales
    left join softcartDimCountry
    on softcartFactSales.countryid = softcartDimCountry.countryid
    group by country
    )
     DATA INITIALLY DEFERRED
     REFRESH DEFERRED
     MAINTAINED BY SYSTEM;
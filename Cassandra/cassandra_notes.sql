--from CLI connect to cassandra
-- start_cassandra

--enter your string in the cli
--cqlsh --username ***** --password *****

--find host details
show host 

--version info
show version

--Create a Keyspace with simple strat
CREATE KEYSPACE training  
WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3};

--list keyspaces
describe keyspaces
describe training 

--create tables
use training;
CREATE TABLE movies(
movie_id int PRIMARY KEY,
movie_name text,
year_of_release int
);

--add a column to tables
ALTER TABLE movies
ADD genre text;

--insert a row into table
INSERT into movies(
movie_id, movie_name, year_of_release)
VALUES (1,'Toy Story',1995);

--update record
UPDATE movies
SET year_of_release = 1996
WHERE movie_id = 4;

--delete record
DELETE from movies WHERE movie_id = 5;

--list tables in a keyspace
describe tables
describe movies

--drop a column
alter table books drop price;

--drop tables
drop table movies;

--alter keyspaces
ALTER KEYSPACE training
WITH replication = {'class': 'NetworkTopologyStrategy'};

--create index
CREATE INDEX user_state
   ON myschema.users (state);

--use a keyspace
use training;

--drop keyspace
drop keyspace training;

--clear screen
cls

--disconnect
exit
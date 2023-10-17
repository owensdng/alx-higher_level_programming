# MySQL Introduction

This repository contains SQL scripts to complete various tasks related to MySQL database management. The tasks cover a range of operations, including creating databases, tables, and performing data manipulation.

## Author
- Noah Owens

## Tasks
1. [List Databases](0-list_databases.sql) - List all databases on the MySQL server.
2. [Create a Database](1-create_database_if_missing.sql) - Create a database if it doesn't exist.
3. [Delete a Database](2-remove_database.sql) - Delete a database if it exists.
4. [List Tables](3-list_tables.sql) - List all tables in a database.
5. [Create First Table](4-first_table.sql) - Create a table named first_table.
6. [Table Description](5-full_table.sql) - Display the full description of the first_table.
7. [List All Table Rows](6-list_values.sql) - List all rows in the first_table.
8. [Insert a Row](7-insert_value.sql) - Insert a new row into the first_table.
9. [Count Records](8-count_89.sql) - Count the number of records with a specific value.
10. [Create Second Table](9-full_creation.sql) - Create a table named second_table and add multiple rows.
11. [List by Score](10-top_score.sql) - List all records ordered by score.
12. [Select the Best](11-best_score.sql) - List records with a score greater than or equal to 10.
13. [Update Score](12-no_cheating.sql) - Update the score for a specific record.
14. [Remove Records](13-change_class.sql) - Remove records with a score less than or equal to 5.
15. [Average Score](14-average.sql) - Compute the average score of all records.
16. [Number by Score](15-groups.sql) - List the number of records for each score.
17. [List Records with Names](16-no_link.sql) - List all records with a name, ordered by score.
18. [Convert to UTF8](100-move_to_utf8.sql) - Convert the database, table, and field to UTF8.
19. [Average Temperatures](101-avg_temperatures.sql) - Display the average temperatures by city.
20. [Top Cities in Summer](102-top_city.sql) - Display the top 3 cities with the highest temperatures in July and August.
21. [Max Temperatures by State](103-max_state.sql) - Display the max temperature of each state.

Each task is contained in a separate SQL file with a brief description.

## Usage
To execute these SQL scripts, you can use a MySQL client or the command line.

Example:
```shell
mysql -h localhost -u root -p < 0-list_databases.sql

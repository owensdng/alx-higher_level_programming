-- Task 0: List databases
SELECT DATABASE(); -- List all databases on the MySQL server.

-- Task 1: Create a database
CREATE DATABASE IF NOT EXISTS hbtn_0c_0; -- Create a new database hbtn_0c_0 if it doesn't exist.

-- Task 2: Delete a database
DROP DATABASE IF EXISTS hbtn_0c_0; -- Delete the hbtn_0c_0 database if it exists.

-- Task 3: List tables
SHOW TABLES FROM hbtn_0c_0; -- List all tables in the hbtn_0c_0 database.

-- Task 4: First table
USE hbtn_0c_0;
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
); -- Create a table named first_table in the hbtn_0c_0 database.

-- Task 5: Full description
DESCRIBE hbtn_0c_0.first_table; -- Show the full description of the first_table.

-- Task 6: List all in table
SELECT * FROM hbtn_0c_0.first_table; -- List all rows in the first_table.

-- Task 7: First add
INSERT INTO hbtn_0c_0.first_table (id, name) VALUES (89, 'Best School'); -- Insert a new row into first_table.

-- Task 8: Count 89
SELECT COUNT(*) FROM hbtn_0c_0.first_table WHERE id = 89; -- Count the number of records with id = 89.

-- Task 9: Full creation
USE hbtn_0c_0;
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
); -- Create a table named second_table in the hbtn_0c_0 database.

INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10), (2, 'Alex', 3), (3, 'Bob', 14), (4, 'George', 8); -- Add multiple rows to second_table.

-- Task 10: List by best
SELECT * FROM hbtn_0c_0.second_table ORDER BY score DESC; -- List all records ordered by score.

-- Task 11: Select the best
SELECT * FROM hbtn_0c_0.second_table WHERE score >= 10 ORDER BY score DESC; -- List records with score >= 10 ordered by score.

-- Task 12: Cheating is bad
UPDATE hbtn_0c_0.second_table SET score = 10 WHERE name = 'Bob'; -- Update the score of Bob to 10.

-- Task 13: Score too low
DELETE FROM hbtn_0c_0.second_table WHERE score <= 5; -- Remove records with score <= 5.

-- Task 14: Average
SELECT AVG(score) AS average FROM hbtn_0c_0.second_table; -- Compute the average score.

-- Task 15: Number by score
SELECT score, COUNT(*) AS number FROM hbtn_0c_0.second_table GROUP BY score ORDER BY number DESC; -- List the number of records for each score.

-- Task 16: Say my name
SELECT score, name FROM hbtn_0c_0.second_table WHERE name IS NOT NULL ORDER BY score DESC; -- List records with a name ordered by score.

-- Task 17: Go to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; -- Convert the hbtn_0c_0 database to UTF8.

ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; -- Convert the first_table to UTF8.

ALTER TABLE hbtn_0c_0.first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; -- Convert the name field to UTF8.

-- Task 18: Temperatures #0
-- Import and execute a SQL script for this task.

-- Task 19: Temperatures #1
-- Import and execute a SQL script for this task.

-- Task 20: Temperatures #2
-- Import and execute a SQL script for this task.

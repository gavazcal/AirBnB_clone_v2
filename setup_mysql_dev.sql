-- Prepares a MySQL server

-- Creates db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creates user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grants privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnd_dev'@'localhost';

-- Grants privileges
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
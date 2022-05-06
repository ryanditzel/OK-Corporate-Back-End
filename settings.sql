-- settings.sql
CREATE DATABASE ok_corporate;
CREATE USER adminuser WITH PASSWORD 'admin';
GRANT ALL PRIVILEGES ON DATABASE ok_corporate TO adminuser;
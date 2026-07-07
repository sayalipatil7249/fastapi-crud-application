CREATE DATABASE crud_app;

USE crud_app;

CREATE TABLE users(
	id INT auto_increment PRIMARY KEY,
    name VARCHAR(100),
    age VARCHAR(100),
    email VARCHAR(100),
    mobile VARCHAR(15),
    password VARCHAR(100)
);

select * from users;
# Streamlit CRUD Operations with MySQL

This project is a simple Streamlit app that demonstrates CRUD (Create, Read, Update, Delete) operations with a MySQL database.

## Features

- Create records in the MySQL database
- Read and display records
- Update records by ID
- Delete records by ID

## Prerequisites

- **Docker**: You will need Docker installed on your machine.
- **MySQL**: Ensure that a MySQL database is running with the necessary credentials and schema.

## MySQL Setup

Make sure you have a MySQL database running locally or remotely. Here's an example SQL command to create the `users` table:

```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    email VARCHAR(50)
);

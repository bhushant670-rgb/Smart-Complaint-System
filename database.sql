CREATE DATABASE college;

USE college;

CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100)
);

CREATE TABLE complaint(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    room INT,
    hostel VARCHAR(100),
    floor INT,
    block VARCHAR(50),
    complaint TEXT,
    email VARCHAR(100),
    UNIQUE(email, room)
);
 CREATE TABLE complaint(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    room INT,
    hostel VARCHAR(100),
    floor INT,
    block VARCHAR(50),
    complaint TEXT,
    email VARCHAR(100),
    status VARCHAR(20) DEFAULT 'pending'
);

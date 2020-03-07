CREATE TABLE Contact(
    id INT AUTO_INCREMENT,
    name VARCHAR(50),
    country_code VARCHAR(5),
    telephone_number VARCHAR(20),
    email VARCHAR(50),
    message TEXT,
    PRIMARY KEY (id)
);
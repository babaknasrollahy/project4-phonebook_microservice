CREATE DATABASE phonebook ;
USE phonebook ;
CREATE TABLE names 
(
        contactID int NOT NULL AUTO_INCREMENT PRIMARY KEY ,
        contactName varchar(100) unique ,
	contactNumber varchar(15)

);


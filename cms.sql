CREATE DATABASE IF NOT EXISTS ParcelDeliveryDB;
USE ParcelDeliveryDB;

CREATE TABLE Branch ( b_id INT PRIMARY KEY,
b_sto_cap INT,
b_loc VARCHAR(100)
);

CREATE TABLE Contact_No ( b_id INT,
b_contact VARCHAR(15), PRIMARY KEY (b_id, b_contact),
FOREIGN KEY (b_id) REFERENCES Branch(b_id)
);

CREATE TABLE Staff ( s_id INT PRIMARY KEY,
s_age INT,
s_sal DECIMAL(10,2),
s_email VARCHAR(100), s_name VARCHAR(100), s_phone VARCHAR(15), b_id INT,
FOREIGN KEY (b_id) REFERENCES Branch(b_id)
);

CREATE TABLE Manager ( s_id INT PRIMARY KEY,
manager_skill VARCHAR(100),
FOREIGN KEY (s_id) REFERENCES Staff(s_id)
);

CREATE TABLE Delivery ( s_id INT PRIMARY KEY,
delivery VARCHAR(100),
FOREIGN KEY (s_id) REFERENCES Staff(s_id)
);

CREATE TABLE Customer ( c_id INT PRIMARY KEY,
c_fname VARCHAR(50), c_mname VARCHAR(50), c_lname VARCHAR(50), c_phone VARCHAR(15), c_email VARCHAR(100), s_id INT,
r_no INT, t_no INT, pay_id INT,
FOREIGN KEY (s_id) REFERENCES Staff(s_id)
 
);

CREATE TABLE Payment ( pay_id INT PRIMARY KEY, pay_date DATE,
pay_amt DECIMAL(10,2), c_id INT,
FOREIGN KEY (c_id) REFERENCES Customer(c_id)
);

CREATE TABLE Tracking ( t_no INT PRIMARY KEY,
current_status VARCHAR(100), current_loc VARCHAR(150), t_time DATETIME,
c_id INT,
FOREIGN KEY (c_id) REFERENCES Customer(c_id)
);
CREATE TABLE Shipment ( ship_id INT PRIMARY KEY, ship_date DATE,
s_id INT,
FOREIGN KEY (s_id) REFERENCES Staff(s_id)
);
CREATE TABLE Product ( p_id INT PRIMARY KEY, p_wt DECIMAL(10,2), p_cat VARCHAR(50), p_des VARCHAR(255)
);

CREATE TABLE Receives ( p_id INT,
c_id INT,
PRIMARY KEY (p_id, c_id),
FOREIGN KEY (p_id) REFERENCES Product(p_id), FOREIGN KEY (c_id) REFERENCES Customer(c_id)
);

CREATE TABLE Is_Of (
ship_id INT, p_id INT,
PRIMARY KEY (ship_id, p_id),
FOREIGN KEY (ship_id) REFERENCES Shipment(ship_id), FOREIGN KEY (p_id) REFERENCES Product(p_id)
);

CREATE TABLE Receipt ( r_no INT PRIMARY KEY,
r_date DATE,
 
total_amt DECIMAL(10,2), s_id INT,
c_id INT,
FOREIGN KEY (s_id) REFERENCES Staff(s_id), FOREIGN KEY (c_id) REFERENCES Customer(c_id)
);

INSERT INTO Branch VALUES (1, 500, 'Mumbai'),
(2, 300, 'Pune'),
(3, 400, 'Nashik');

INSERT INTO Contact_No VALUES (1, '9876543210'),
(2, '9876543211'),
(3, '9876543212');

INSERT INTO Staff VALUES
(101, 35, 45000, 'amit@gmail.com', 'Amit Sharma', '9000000001', 1),
(102, 29, 35000, 'neha@gmail.com', 'Neha Patil', '9000000002', 2),
(103, 32, 40000, 'rahul@gmail.com', 'Rahul Mehta', '9000000003', 3);

INSERT INTO Manager VALUES
(101, 'Operations Management'),
(102, 'Team Management'),
(103, 'Logistics Management');

INSERT INTO Delivery VALUES
(101, 'Local Delivery'),
(102, 'Express Delivery'),
(103, 'Regional Delivery');

INSERT INTO Customer VALUES
(201, 'Raj', 'Kumar', 'Shah', '9111111111', 'raj@gmail.com', 101, 301, 401, 501),
(202, 'Priya', 'Sunil', 'Desai', '9222222222', 'priya@gmail.com', 102, 302, 402, 502),
(203, 'Aarav', 'Raj', 'Joshi', '9333333333', 'aarav@gmail.com', 103, 303, 403, 503);

INSERT INTO Payment VALUES (501, '2026-10-10', 500.00, 201),
(502, '2026-10-11', 750.00, 202),
(503, '2026-10-12', 300.00, 203);

INSERT INTO Tracking VALUES
(401, 'In Transit', 'Mumbai', '2026-10-15 10:30:00', 201),
(402, 'Out for Delivery', 'Pune', '2026-10-15 11:00:00', 202),
(403, 'Delivered', 'Nashik', '2026-10-15 12:00:00', 203);

INSERT INTO Shipment VALUES (601, '2026-10-10', 101),
(602, '2026-10-11', 102),
(603, '2026-10-12', 103);
 
INSERT INTO Product VALUES
(701, 2.50, 'Electronics', 'Wireless Headphones'),
(702, 1.20, 'Clothing', 'Cotton Shirt'),
(703, 5.00, 'Books', 'Academic Books');

INSERT INTO Receives VALUES (701, 201),
(702, 202),
(703, 203);

INSERT INTO Is_Of VALUES (601, 701),
(602, 702),
(603, 703);

INSERT INTO Receipt VALUES (301, '2026-10-10', 500.00, 101, 201),
(302, '2026-10-11', 750.00, 102, 202),
(303, '2026-10-12', 300.00, 103, 203);

DESCRIBE Branch;
DESCRIBE Contact_No;
DESCRIBE Staff;
DESCRIBE Manager;
DESCRIBE Delivery;
DESCRIBE Customer;
DESCRIBE Payment;
DESCRIBE Tracking;
DESCRIBE Shipment;
DESCRIBE Product;
DESCRIBE Receives;
DESCRIBE Is_Of;
DESCRIBE Receipt;

SELECT * FROM Branch; SELECT * FROM Contact_No; SELECT * FROM Staff;
SELECT * FROM Manager; SELECT * FROM Delivery; SELECT * FROM Customer; SELECT * FROM Payment; SELECT * FROM Tracking; SELECT * FROM Shipment; SELECT * FROM Product; SELECT * FROM Receives; SELECT * FROM Is_Of;
SELECT * FROM Receipt;

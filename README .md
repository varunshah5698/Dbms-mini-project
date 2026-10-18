# 📦 Courier Management System

A database-driven desktop application mini-project for managing parcel-related records using **Python, Tkinter, and MySQL**. The project demonstrates relational database design, SQL operations, primary and foreign keys, and Python–MySQL connectivity.

## 👥 Contributors

| Roll No. | Name | SAP ID |
|---|---|---|
| S038 | Parshva Julesh Shah | 60018250091 |
| S053 | Tanish Sanjay Rajput | 60018250021 |
| S055 | Varun Nitin Shah | 60018250008 |
| S056 | Vedant Dashrath Bhoir | 60018250098 |

- **Department:** Artificial Intelligence and Data Science
- **Institute:** Dwarkadas J. Sanghvi College of Engineering (DJSCE), Mumbai
- **Course:** Database Management System Laboratory
- **Academic year:** 2026–2027
- **Semester:** III
- **Division:** S
- **Batch:** A-2

## 📌 Project Overview

Courier services maintain information about customers, staff, branches, parcels, shipments, tracking records, receipts, and payments. Keeping these records in separate registers or spreadsheets can make information harder to organise and maintain consistently.

This project models courier operations in a MySQL relational database named `ParcelDeliveryDB`. The schema includes tables for branches, branch contact numbers, staff, managers, delivery staff, customers, payments, tracking, shipments, products, product–customer relationships, shipment–product relationships, and receipts.

The included Python desktop application demonstrates **Create, Read, Update, and Delete (CRUD) operations on product records**. A separate window displays product records retrieved from MySQL. The GUI does not currently expose CRUD screens for every table in the database.

## ✨ Implemented Features

- **Insert products:** Add a product ID, weight, category, and description.
- **Update products:** Modify a product's weight, category, and description using its product ID.
- **Delete products:** Delete a product after confirmation.
- **View products:** Display product records from the database in a separate window.
- **Input checks:** Validate required product fields and require a positive weight.
- **Database error handling:** Show error messages for database failures and roll back failed write operations.
- **Relational schema:** Use primary keys and foreign keys to represent relationships between courier-related records.

## 🧰 Technology Stack

| Component | Technology |
|---|---|
| Programming language | Python 3.x |
| GUI | Tkinter |
| Database | MySQL |
| Python database connector | `mysql-connector-python` |
| Database tool (optional) | MySQL Workbench |

## 💻 Requirements

### Software
- Python 3.x
- MySQL Server
- `mysql-connector-python`
- MySQL Workbench (optional; MySQL CLI can also be used)

### Hardware
- Processor: Intel Core i3 / AMD Ryzen 3 or equivalent
- RAM: 4 GB or more
- Free storage: approximately 1 GB
- Display: 1366 × 768 or higher
- Keyboard and mouse

## 📂 Project Structure

The repository is expected to contain the following files. Check the actual repository if a filename or location differs.

```text
Dbms-mini-project/
├── main.py       # Main Tkinter window for product CRUD operations
├── next_win.py   # Separate window to view product records
├── schema.sql    # Database schema and, if included, sample data
├── Report.pdf    # Mini-project report
└── README.md     # Project documentation
```

## 🚀 Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/varunshah5698/Dbms-mini-project.git
cd Dbms-mini-project
```

### 2. Create the database and tables

If `schema.sql` is present and contains the complete table definitions, run it using MySQL Workbench or the MySQL command-line client:

```bash
mysql -u root -p < schema.sql
```

Enter your MySQL password when prompted.

If the SQL file contains only table definitions, it will create the schema but may not insert sample records. If the repository does not contain `schema.sql`, use the MySQL code documented in the project report to create the database and tables. Run the SQL setup only once on a clean database, unless you have confirmed it is safe to rerun.

### 3. Install the Python dependency

```bash
python -m pip install mysql-connector-python
```

On some systems, use `python3` instead of `python`.

### 4. Configure the MySQL connection

The application connects to the local MySQL database `ParcelDeliveryDB`. In both `main.py` and `next_win.py`, configure the connection with your own local MySQL credentials.

Example:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_LOCAL_MYSQL_PASSWORD",
    database="ParcelDeliveryDB"
)
```

Replace the placeholder with your local MySQL password. **Do not commit real passwords or other credentials to GitHub.**

### 5. Run the application

```bash
python main.py
```

Use the main window to insert, update, or delete product records. Select **View Products** to open the product viewer.

## 🧪 Demonstrated Operations

The project report documents the following product-management scenarios:

- Viewing existing product records.
- Inserting a product (example ID: `705`).
- Updating a product (the report references ID `704`).
- Deleting product ID `705`.

These are report examples, not a guarantee that the same records exist in every database instance. Ensure the relevant product records exist before repeating the scenarios.

## 🗃️ Database Design

The schema in the report includes the following tables:

- `Branch`
- `Contact_No`
- `Staff`
- `Manager`
- `Delivery`
- `Customer`
- `Payment`
- `Tracking`
- `Shipment`
- `Product`
- `Receives`
- `Is_Of`
- `Receipt`

Primary keys identify records, while foreign keys define relationships between related tables. See the SQL schema and the ER diagram in the project report for the detailed design.

## 📸 Screenshots and Report

The accompanying mini-project report documents the application window, product-table display, and insert, update, and delete examples. Refer to `Report.pdf` for the ER diagram, requirements, code, SQL, and output screenshots.

If you add screenshots to the repository, you can create a `screenshots/` folder and link them here.

## ⚠️ Notes and Limitations

- The current GUI focuses on product CRUD and product viewing; it is not a complete GUI for every table in the database.
- The viewer query in the supplied code displays up to 10 product records.
- Database setup and sample records depend on the SQL file included in the repository.
- Keep database credentials private and configure them locally.

## 📄 Academic Context

This project was developed as part of the Database Management System Laboratory coursework at Dwarkadas J. Sanghvi College of Engineering, Mumbai, for academic year 2026–2027.

## 🔗 Repository

[GitHub Repository](https://github.com/varunshah5698/Dbms-mini-project)

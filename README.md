# 🛒 Retail Sales ETL & Analytics Pipeline

An end-to-end **Retail Sales ETL and Analytics project** built using **Python, Pandas, PostgreSQL, SQL, and Power BI**.

This project demonstrates how raw retail sales data can be extracted from CSV files, cleaned and transformed using Python, stored in PostgreSQL, analyzed using SQL, and visualized through an interactive Power BI dashboard.

---

## 📌 Project Overview

The objective of this project is to build a simple and practical **data engineering pipeline** for retail sales data.

The pipeline performs:

* Data extraction from CSV files
* Data cleaning and validation
* Data transformation using Python and Pandas
* Calculation of order revenue
* Loading processed data into PostgreSQL
* SQL-based data analysis
* Power BI dashboard development

---

## 🏗️ Project Architecture

```text
             ┌─────────────────┐
             │   CSV Files     │
             │                 │
             │ Customers       │
             │ Products        │
             │ Orders          │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Python + Pandas │
             │                 │
             │ Extract         │
             │ Clean           │
             │ Transform       │
             │ Validate        │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │   PostgreSQL    │
             │                 │
             │ Customers       │
             │ Products        │
             │ Orders          │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │      SQL        │
             │                 │
             │ Sales Analysis  │
             │ Revenue Analysis│
             │ Product Analysis│
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │     Power BI    │
             │                 │
             │ KPI Cards       │
             │ Charts          │
             │ Sales Dashboard │
             └─────────────────┘
```

---

## 🛠️ Technologies Used

| Technology   | Purpose                          |
| ------------ | -------------------------------- |
| Python       | ETL development                  |
| Pandas       | Data cleaning and transformation |
| PostgreSQL   | Data storage                     |
| SQL          | Data analysis                    |
| Power BI     | Data visualization               |
| CSV          | Raw data source                  |
| Git & GitHub | Version control                  |

---

## 📂 Project Structure

```text
Retail-Sales-ETL-Project/
│
├── data/
│   ├── customers.csv
│   ├── products.csv
│   └── orders.csv
│
├── scripts/
│   └── etl_pipeline.py
│
├── sql/
│   └── analysis.sql
│
├── output/
│   ├── cleaned_customers.csv
│   ├── cleaned_products.csv
│   └── cleaned_orders.csv
│
├── .gitignore
└── README.md
```

---

## 📊 Dataset

The project uses three CSV files.

### Customers

Contains customer information:

* Customer ID
* Customer Name
* Email
* City
* Signup Date

### Products

Contains product information:

* Product ID
* Product Name
* Category
* Price

### Orders

Contains sales transaction information:

* Order ID
* Customer ID
* Product ID
* Order Date
* Quantity
* Payment Method

---

## 🔄 ETL Process

### 1. Extract

The pipeline reads the raw CSV files using Pandas.

```python
customers = pd.read_csv("data/customers.csv")
products = pd.read_csv("data/products.csv")
orders = pd.read_csv("data/orders.csv")
```

### 2. Transform

The data is cleaned and transformed by:

* Removing duplicate records
* Removing unnecessary spaces
* Standardizing email values
* Converting dates into proper date format
* Converting numeric columns into appropriate data types
* Validating quantities
* Validating product prices
* Joining orders with product information
* Calculating total order amount

The revenue calculation is:

```text
Total Amount = Quantity × Product Price
```

### 3. Load

The transformed data is loaded into PostgreSQL tables:

```text
customers
products
orders
```

Duplicate records are handled using PostgreSQL conflict handling.

---

## 🗄️ PostgreSQL Database

The database contains three main tables.

### Customers

```text
customer_id
customer_name
email
city
signup_date
```

### Products

```text
product_id
product_name
category
price
```

### Orders

```text
order_id
customer_id
product_id
order_date
quantity
payment_method
total_amount
```

---

## 🔎 SQL Analysis

SQL queries are used to analyze the processed retail data.

Examples include:

* Total revenue
* Total orders
* Product-wise revenue
* City-wise revenue
* Payment-method analysis
* Monthly sales
* Customer purchase analysis
* Top-performing products

---

## 📈 Power BI Dashboard

The processed PostgreSQL data is connected to Power BI to create an interactive sales dashboard.

### Dashboard KPIs

| KPI                 |   Result |
| ------------------- | -------: |
| Total Revenue       | ₹352,100 |
| Total Orders        |       16 |
| Total Quantity Sold |       38 |
| Total Customers     |        8 |

### Dashboard Visualizations

The dashboard includes:

* Total Revenue KPI
* Total Orders KPI
* Total Quantity KPI
* Total Customers KPI
* Revenue by Product
* Revenue by City
* Monthly Revenue
* Revenue by Payment Method
* Product Performance

---

## 💰 Revenue Analysis

### Revenue by Product

| Product    |      Revenue |
| ---------- | -----------: |
| Laptop     |     ₹165,000 |
| Mobile     |     ₹125,000 |
| Monitor    |      ₹24,000 |
| Headphones |      ₹18,000 |
| Keyboard   |      ₹10,500 |
| Mouse      |       ₹9,600 |
| **Total**  | **₹352,100** |

### Revenue by City

| City      |      Revenue |
| --------- | -----------: |
| Pune      |     ₹137,400 |
| Mumbai    |     ₹125,000 |
| Nagpur    |      ₹53,000 |
| Nashik    |      ₹21,500 |
| Solapur   |      ₹15,200 |
| **Total** | **₹352,100** |

### Revenue by Payment Method

| Payment Method |      Revenue |
| -------------- | -----------: |
| Card           |     ₹188,000 |
| UPI            |     ₹149,600 |
| Cash           |      ₹14,500 |
| **Total**      | **₹352,100** |

### Monthly Revenue

| Month      |      Revenue |
| ---------- | -----------: |
| April 2026 |     ₹158,200 |
| May 2026   |     ₹193,900 |
| **Total**  | **₹352,100** |


## 🎯 Key Learning Outcomes

Through this project, I practiced:

* Building an ETL pipeline
* Python data processing
* Pandas data cleaning
* Data validation
* PostgreSQL database operations
* SQL queries and analysis
* Relational data handling
* Data visualization
* Power BI dashboard development
* Git and GitHub version control

---

## 💼 Skills Demonstrated

```text
Python
Pandas
SQL
PostgreSQL
ETL
Data Cleaning
Data Transformation
Data Validation
Power BI
Data Visualization
Git
GitHub
```

---

## 👨‍💻 Author

**Nikhil Shinde**

B.Tech Computer Science & Engineering

Interested in:

* Data Engineering
* Data Analytics
* Python
* SQL
* ETL
* Cloud Data Technologies

---

## ⭐ Project Highlights

* End-to-end ETL pipeline
* Automated data cleaning and transformation
* PostgreSQL data warehouse-style storage
* SQL analytical queries
* Interactive Power BI dashboard
* GitHub version-controlled project

---

## 📜 License

This project is created for educational and portfolio purposes.

import pandas as pd
import psycopg2
from pathlib import Path


# -----------------------------
# 1. File Paths
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

CUSTOMERS_FILE = BASE_DIR / "data" / "customers.csv"
PRODUCTS_FILE = BASE_DIR / "data" / "products.csv"
ORDERS_FILE = BASE_DIR / "data" / "orders.csv"

OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


# -----------------------------
# 2. EXTRACT
# -----------------------------

print("Starting ETL Pipeline...")

customers = pd.read_csv(CUSTOMERS_FILE)
products = pd.read_csv(PRODUCTS_FILE)
orders = pd.read_csv(ORDERS_FILE)

print("Data extracted successfully.")

print("Customers:", len(customers))
print("Products:", len(products))
print("Orders:", len(orders))


# -----------------------------
# 3. TRANSFORM CUSTOMERS
# -----------------------------

customers = customers.drop_duplicates(
    subset=["customer_id"]
)

customers["email"] = customers["email"].str.lower().str.strip()

customers["customer_name"] = (
    customers["customer_name"].str.strip()
)

customers["city"] = customers["city"].str.strip()

customers["signup_date"] = pd.to_datetime(
    customers["signup_date"],
    errors="coerce"
)


# -----------------------------
# 4. TRANSFORM PRODUCTS
# -----------------------------

products = products.drop_duplicates(
    subset=["product_id"]
)

products["product_name"] = (
    products["product_name"].str.strip()
)

products["category"] = (
    products["category"].str.strip()
)

products["price"] = pd.to_numeric(
    products["price"],
    errors="coerce"
)

products = products.dropna(
    subset=["product_id", "price"]
)


# -----------------------------
# 5. TRANSFORM ORDERS
# -----------------------------

orders = orders.drop_duplicates(
    subset=["order_id"]
)

orders["order_date"] = pd.to_datetime(
    orders["order_date"],
    errors="coerce"
)

orders["quantity"] = pd.to_numeric(
    orders["quantity"],
    errors="coerce"
)

orders["payment_method"] = (
    orders["payment_method"].str.strip()
)


# -----------------------------
# 6. JOIN ORDERS + PRODUCTS
# -----------------------------

orders = orders.merge(
    products[["product_id", "price"]],
    on="product_id",
    how="left"
)


# -----------------------------
# 7. CALCULATE TOTAL AMOUNT
# -----------------------------

orders["total_amount"] = (
    orders["quantity"] * orders["price"]
)


# -----------------------------
# 8. DATA VALIDATION
# -----------------------------

orders = orders.dropna(
    subset=[
        "order_id",
        "customer_id",
        "product_id",
        "order_date",
        "quantity",
        "price"
    ]
)

orders = orders[
    orders["quantity"] > 0
]

orders = orders[
    orders["price"] >= 0
]


# -----------------------------
# 9. SELECT FINAL COLUMNS
# -----------------------------

orders = orders[
    [
        "order_id",
        "customer_id",
        "product_id",
        "order_date",
        "quantity",
        "payment_method",
        "total_amount"
    ]
]


# -----------------------------
# 10. SAVE CLEANED DATA
# -----------------------------

customers.to_csv(
    OUTPUT_DIR / "cleaned_customers.csv",
    index=False
)

products.to_csv(
    OUTPUT_DIR / "cleaned_products.csv",
    index=False
)

orders.to_csv(
    OUTPUT_DIR / "cleaned_orders.csv",
    index=False
)

print("Data transformation completed.")

import os
from dotenv import load_dotenv

load_dotenv()

# 11. POSTGRESQL CONNECTION
# -----------------------------

conn = psycopg2.connect(
    host="localhost",
    database="retail_etl_db",
    user="postgres",
    password=os.getenv("POSTGRES_PASSWORD"),
    port="5432"
)

cursor = conn.cursor()

# -----------------------------
# 12. LOAD CUSTOMERS
# -----------------------------

for _, row in customers.iterrows():

    cursor.execute(
        """
        INSERT INTO customers
        (customer_id, customer_name, email, city, signup_date)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (customer_id)
        DO NOTHING;
        """,
        (
            int(row["customer_id"]),
            row["customer_name"],
            row["email"],
            row["city"],
            row["signup_date"]
        )
    )


# -----------------------------
# 13. LOAD PRODUCTS
# -----------------------------

for _, row in products.iterrows():

    cursor.execute(
        """
        INSERT INTO products
        (product_id, product_name, category, price)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (product_id)
        DO NOTHING;
        """,
        (
            row["product_id"],
            row["product_name"],
            row["category"],
            float(row["price"])
        )
    )


# -----------------------------
# 14. LOAD ORDERS
# -----------------------------

for _, row in orders.iterrows():

    cursor.execute(
        """
        INSERT INTO orders
        (
            order_id,
            customer_id,
            product_id,
            order_date,
            quantity,
            payment_method,
            total_amount
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (order_id)
        DO NOTHING;
        """,
        (
            row["order_id"],
            int(row["customer_id"]),
            row["product_id"],
            row["order_date"],
            int(row["quantity"]),
            row["payment_method"],
            float(row["total_amount"])
        )
    )

# -----------------------------
# 15. COMMIT
# -----------------------------

conn.commit()

cursor.close()
conn.close()
print("Data loaded successfully into PostgreSQL.")
print("ETL Pipeline completed successfully!")
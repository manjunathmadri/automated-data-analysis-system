import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Manjunath@45",
    database="automated_analysis"
)
cursor = conn.cursor()


def get_table_columns(table):
    cursor.execute(f"SHOW COLUMNS FROM {table}")
    return [row[0] for row in cursor.fetchall()]


def load_csv(file, table):
    try:
        df = pd.read_csv(file)

        # normalize headers
        df.columns = df.columns.str.strip().str.lower()

        # rename mismatched columns
        rename_map = {
            "name": "product_name",
            "product_id": "productid"
        }
        df.rename(columns=rename_map, inplace=True)

        db_cols = get_table_columns(table)

        # remove id if auto increment
        if "id" in db_cols and "id" in df.columns:
            df = df.drop(columns=["id"])

        # keep only matching columns
        df = df[[col for col in df.columns if col in db_cols]]

        cols = ",".join(df.columns)
        vals = ",".join(["%s"] * len(df.columns))
        sql = f"INSERT IGNORE INTO {table} ({cols}) VALUES ({vals})"

        for row in df.itertuples(index=False):
            cursor.execute(sql, tuple(row))

        conn.commit()
        print(f"✅ {table} loaded ({len(df)} rows)")

    except Exception as e:
        print(f"❌ Error loading {table}: {e}")


load_csv("Data/users.csv", "users")
load_csv("Data/products.csv", "products")
load_csv("Data/orders.csv", "orders")

cursor.close()
conn.close()
print("🎉 All data imported successfully!")
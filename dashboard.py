import streamlit as st
import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Manjunath@45",
    database="automated_analysis"
)

st.title("📊 Automated Data Analysis Dashboard")

menu = st.sidebar.selectbox("Select Data", ["Users", "Products", "Orders", "Reports"])

query_map = {
    "Users": "SELECT * FROM users",
    "Products": "SELECT * FROM products",
    "Orders": "SELECT * FROM orders",
    "Reports": "SELECT * FROM reports"
}

df = pd.read_sql(query_map[menu], conn)

st.subheader(menu + " Data")
st.dataframe(df)

if menu == "Reports" and not df.empty:
    st.metric("Total Sales", df.iloc[-1]["total_sales"])
    st.metric("Total Orders", df.iloc[-1]["total_orders"])

conn.close()
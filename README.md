# 📊 Automated Data Analysis System

An End-to-End Automated Data Analysis & Reporting System built using:

- Python
- MySQL
- Streamlit
- ReportLab
- Matplotlib

This project simulates a real-world e-commerce analytics system with database integration, dashboard visualization, and automated PDF report generation.

---

## 🚀 Project Overview

This system:

✔ Loads CSV data into MySQL  
✔ Performs relational analysis (Users, Products, Orders)  
✔ Displays interactive dashboard using Streamlit  
✔ Generates professional multi-page PDF reports with charts  
✔ Allows direct download of reports  

---

## 🏗️ Project Architecture

```
AUTOMATED DATA ANALYSIS SYSTEM
│
├── config/                  # Database configuration
│
├── DASHBOARD_SNAPS/         # Dashboard screenshots
│   ├── dashboard.png
│   ├── order.png
│   ├── product.png
│   ├── user.png
│
├── data/                    # CSV dataset
│   ├── users.csv
│   ├── products.csv
│   ├── orders.csv
│
├── models/                  # SQL schema
│   ├── schema.sql
│
├── outputs/                 # Generated reports & charts
│   ├── professional_report.pdf
│   ├── sales_chart.png
│
├── services/                # Business logic layer
│   ├── user_service.py
│   ├── product_service.py
│   ├── order_service.py
│   ├── report_service.py
│   ├── pdf_service.py
│
├── utils/                   # Utility helpers
│   ├── logger.py
│
├── load_data.py             # Load CSV into MySQL
├── dashboard.py             # Streamlit dashboard
├── main.py                  # Backend entry point
├── requirements.txt
├── README.md
└── .env
```

---

## ✨ Features

### 📂 Data Layer
- Structured relational schema
- Users, Products, Orders normalization
- MySQL database integration

### 📊 Dashboard (Streamlit)
- Total Orders metric
- Total Revenue metric
- Orders data table
- Sales by user visualization
- Interactive UI
- Downloadable PDF report

### 📄 Professional PDF Report
- Auto-generated multi-page layout
- Summary section
- Styled data table
- Bar chart
- Pie chart
- Top customer detection
- Timestamp included

---

## 📊 Dashboard Preview

### 🏠 Main Dashboard
![Dashboard](DASHBOARD_SNAPS/dashboard.png)

### 🛒 Orders View
![Orders](DASHBOARD_SNAPS/order.png)

### 📦 Products View
![Products](DASHBOARD_SNAPS/product.png)

### 👤 Users View
![Users](DASHBOARD_SNAPS/user.png)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd automated-data-analysis-system
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ Database Setup

1. Open MySQL
2. Create database:

```sql
CREATE DATABASE automated_analysis;
```

3. Update credentials inside:

```
config/db_config.py
```

4. Run schema:

```bash
mysql -u root -p automated_analysis < models/schema.sql
```

---

## ▶️ Run Application

### Load CSV Data

```bash
python load_data.py
```

### Run Backend

```bash
python main.py
```

### Run Dashboard

```bash
streamlit run dashboard.py
```

---

## 📥 Generate Report

Inside dashboard:

Click  
👉 **Generate & Download Report**

It creates a professional PDF inside `/outputs`.

---

## 🧠 Technical Concepts Used

- Layered Architecture (Config → Services → Dashboard)
- SQL Joins & Aggregations
- Data Normalization
- Report Automation
- Chart Visualization
- Backend-Frontend Integration
- Environment Configuration (.env)

---

## 💼 Skills Demonstrated

- Python Backend Development
- Database Design (MySQL)
- Data Analysis
- Report Automation
- Data Visualization
- Dashboard Development
- Clean Project Structuring
- Git Version Control

---

## 🔮 Future Enhancements

- User authentication
- Date range filtering
- CSV upload via dashboard
- Email report automation
- Cloud deployment (Streamlit Cloud / Render)
- REST API integration

---

## 👨‍💻 Author

Manjunath Madari 
Final Year CS&E Student  
Aspiring Data Analyst & ML Engineer

---
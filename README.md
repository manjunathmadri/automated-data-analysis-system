# 📊 Automated Data Analysis System

An End-to-End Automated Data Analysis System built using:

- Python
- MySQL
- Streamlit
- ReportLab (PDF Generation)
- Matplotlib (Charts)

---

## 🚀 Project Overview

This project loads CSV data into MySQL, performs data analysis, generates reports, and provides an interactive dashboard with downloadable professional PDF reports.

It simulates a real-world e-commerce analytics workflow.

---

## ✨ Features

### 📂 Data Management
- Load CSV data into MySQL
- Structured relational database (Users, Products, Orders)

### 📊 Dashboard (Streamlit)
- Interactive metrics
- Orders table view
- Sales by user chart
- Real-time data visualization

### 📄 Professional PDF Report
- Auto-generated multi-page PDF
- Summary section
- Styled table
- Bar chart
- Pie chart
- Top customer detection
- Timestamp included
- Downloadable directly from dashboard

---

## 📊 Dashboard Preview

### 🏠 Main Dashboard
![Dashboard](DARSHBOARD_SNAPS/dashboard.png)

### 📦 Products View
![Products](DARSHBOARD_SNAPS/product.png)

### 🛒 Orders View
![Orders](DARSHBOARD_SNAPS/order.png)

### 👤 Users View
![Users](DARSHBOARD_SNAPS/user.png)

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd automated-data-analysis-system
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

## 🗄️ Setup MySQL Database

1. Create database:

```sql
CREATE DATABASE automated_analysis;
```

2. Update database credentials in:

```
config/db_config.py
```

---

## ▶️ Run Project

### Run Backend Script

```bash
python main.py
```

### Run Streamlit Dashboard

```bash
streamlit run app.py
```

---

## 📥 Download Report

Inside the dashboard:

Click  
👉 **Generate & Download Report**

It generates a professional multi-page PDF with charts and summary.

---

## 💼 Skills Demonstrated

- Python Backend Development
- MySQL Database Integration
- Data Analysis & Aggregation
- Report Automation
- PDF Generation
- Data Visualization
- Dashboard Development
- End-to-End Project Architecture

---

## 🔥 Future Improvements

- User authentication
- Date filtering
- CSV upload from dashboard
- Email automated report
- Deployment on Streamlit Cloud
- Role-based access

---

## 👨‍💻 Author

Manjunath Madari 
Final Year CS&E Student  
Aspiring Data Analyst & ML Engineer

---
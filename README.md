# 📊 E-commerce Consumer Behavior Dashboard

This project analyzes e-commerce customer behavior to extract valuable business insights using Python. It includes visualizations and key metrics to help understand customer preferences, sales trends, and product performance.

## 🚀 Project Overview

E-commerce platforms generate vast amounts of data every day. By exploring and visualizing this data, businesses can improve marketing strategies, optimize product offerings, and enhance customer satisfaction.

This dashboard focuses on:
- **Sales trends over time**
- **Top-selling products**
- **Revenue by country**
- **Customer purchasing patterns**
- **Frequently used words in product titles**

## 🧾 Dataset

- Filename: `data.csv`
- Contains thousands of rows of e-commerce transactions
- Key columns:
  - `InvoiceNo`
  - `StockCode`
  - `Description`
  - `Quantity`
  - `InvoiceDate`
  - `UnitPrice`
  - `CustomerID`
  - `Country`

> *Note: Data source is publicly available and suitable for educational use.*

## 📌 Features & Insights

- 📈 Monthly revenue trend line
- 🌍 Revenue distribution by country (Bar Chart)
- 🏆 Top 10 selling products (Bar Chart)
- 💰 Revenue per product
- ☁️ WordCloud of most common product descriptions

## 🛠️ Technologies Used

- Python 3
- pandas
- matplotlib
- seaborn
- plotly
- wordcloud

## 🧼 Data Cleaning & Preprocessing

- Removed rows with missing `CustomerID` and `Description`
- Filtered out negative quantities
- Converted `InvoiceDate` to datetime format
- Added `Revenue` column (`Quantity × UnitPrice`)
- Extracted `Month` from `InvoiceDate` for time-based analysis

## 📂 Project Structure


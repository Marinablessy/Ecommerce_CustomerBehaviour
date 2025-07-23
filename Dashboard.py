import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("data.csv", encoding='ISO-8859-1')
    df.dropna(subset=['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country'], inplace=True)
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df = df[df['Country'] == 'United Kingdom']
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    return df

df = load_data()

# Header
st.title("🛍️ UK E-Commerce Dashboard")
st.markdown("Get insights on sales, customer behavior, and top-performing products!")

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"£{df['TotalPrice'].sum():,.0f}")
col2.metric("Unique Customers", df['CustomerID'].nunique())
col3.metric("Total Transactions", df['InvoiceNo'].nunique())

st.markdown("---")

# 1. Monthly Revenue Trend
st.subheader("📈 Monthly Revenue Trend")
df['Month'] = df['InvoiceDate'].dt.to_period('M').astype(str)
monthly_revenue = df.groupby('Month')['TotalPrice'].sum().reset_index()

fig1, ax1 = plt.subplots(figsize=(10, 4))
sns.lineplot(data=monthly_revenue, x='Month', y='TotalPrice', marker='o', ax=ax1)
plt.xticks(rotation=45)
plt.ylabel("Revenue (£)")
plt.title("Monthly Revenue Trend")
st.pyplot(fig1)

# 2. Top 10 Products by Sales
st.subheader("🏆 Top 10 Best-Selling Products")
top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)

fig2, ax2 = plt.subplots(figsize=(10, 4))
sns.barplot(y=top_products.index, x=top_products.values, palette="viridis", ax=ax2)
plt.title("Top 10 Products by Quantity Sold")
plt.xlabel("Units Sold")
plt.ylabel("Product")
st.pyplot(fig2)

# 3. Revenue by Hour of Day
st.subheader("⏰ Revenue by Hour of Day")
df['Hour'] = df['InvoiceDate'].dt.hour
hourly = df.groupby('Hour')['TotalPrice'].sum().reset_index()

fig3, ax3 = plt.subplots()
sns.barplot(data=hourly, x='Hour', y='TotalPrice', palette="coolwarm", ax=ax3)
plt.title("Revenue by Hour of the Day")
plt.ylabel("Revenue (£)")
st.pyplot(fig3)

# 4. Top Customers
st.subheader("💰 Top 5 Customers by Revenue")
top_customers = df.groupby('CustomerID')['TotalPrice'].sum().sort_values(ascending=False).head(5)

fig4, ax4 = plt.subplots()
sns.barplot(x=top_customers.index.astype(str), y=top_customers.values, palette="Blues_d", ax=ax4)
plt.title("Top 5 Customers")
plt.xlabel("Customer ID")
plt.ylabel("Total Revenue (£)")
st.pyplot(fig4)

# 5. Word Cloud of Most Sold Products
st.subheader("🛒 Word Cloud of Product Descriptions")
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(df['Description']))
fig5, ax5 = plt.subplots(figsize=(10, 5))
ax5.imshow(wordcloud, interpolation='bilinear')
ax5.axis('off')
st.pyplot(fig5)

# 6. Recency-Frequency-Monetary (RFM) Segmentation
st.subheader("📊 Customer Segmentation (RFM)")

# RFM Calculation
snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
    'InvoiceNo': 'nunique',
    'TotalPrice': 'sum'
}).reset_index()
rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']

# Show sample of RFM table
st.dataframe(rfm.sort_values(by='Monetary', ascending=False).head())

# Optional Download
st.download_button("📥 Download Cleaned Data", df.to_csv(index=False), "cleaned_data.csv", "text/csv")

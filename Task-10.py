#=======================================
# 10. Data Visualization Dashboard 
# Create visual insights from the dataset. 
# Tasks 
# Create visualizations: 
# • Sales by region 
# • Top 10 products 
# • Monthly sales trend 
# • Profit distribution 
# • Boxplot for outliers 
# Skills Practiced 
# • Matplotlib 
# • Seaborn 
# • Data storytelling
#========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =========================================
# 10. Data Visualization Dashboard
# =========================================

# Load dataset
df = pd.read_csv("sales_dataset-2_cleaned.csv")
print("\nCleaned Dataset :",df)

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Convert numeric columns
df['sales_amount'] = pd.to_numeric(df['sales_amount'], errors='coerce')
df['profit_amount'] = pd.to_numeric(df['profit_amount'], errors='coerce')
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')

# Convert order_date
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

# Extract month
df['month'] = df['order_date'].dt.to_period('M')

# --------------------------------------------
# Create Dashboard Layout
# --------------------------------------------

plt.figure(figsize=(15,10))

# --------------------------------------------
# 1. Sales by Region
# --------------------------------------------

plt.subplot(2,3,1)

region_sales = df.groupby('region')['sales_amount'].sum().sort_values()

region_sales.plot(kind='bar', color='skyblue')

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

# --------------------------------------------
# 2. Top 10 Products by Revenue
# --------------------------------------------

plt.subplot(2,3,2)

top_products = df.groupby('product_name')['sales_amount'].sum()\
                 .sort_values(ascending=False)\
                 .head(10)

top_products.plot(kind='bar', color='orange')

plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")

# --------------------------------------------
# 3. Monthly Sales Trend
# --------------------------------------------

plt.subplot(2,3,3)

monthly_sales = df.groupby('month')['sales_amount'].sum()

monthly_sales.plot(kind='line', marker='o', color='green')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

# --------------------------------------------
# 4. Profit Distribution
# --------------------------------------------

plt.subplot(2,3,4)

sns.histplot(df['profit_amount'], bins=30, kde=True)

plt.title("Profit Distribution")

# --------------------------------------------
# 5. Boxplot for Sales Outliers
# --------------------------------------------

plt.subplot(2,3,5)

sns.boxplot(x=df['sales_amount'])

plt.title("Sales Outliers (Boxplot)")

# --------------------------------------------
# Layout adjustment
# --------------------------------------------

plt.tight_layout()

plt.show()
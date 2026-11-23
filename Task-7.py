
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#  *****************************   7.   Montly Sales Trend   ***************************

# Task 
# Extract Months from order dates
# Calculate monthly sales
# Plot montly sales trend.

# Skills Precticed
# ---- Time series analysis
# ---- Line charts


# Load Data

df = pd.read_csv("sales_dataset-2_cleaned.csv")
print('Clean Data:',df)
print("Head",df.head(10))
print("Tail:",df.tail(10))
print("Describe:",df.describe())
print("Info:",df.info())
print("shape:",df.shape)


# Clean columns name 
df.columns = df.columns.str.strip().str.lower()
print("clean columns name:",df.columns)


# convert data type into datetime
# convert sales_amount into numeric

df['order_date'] = pd.to_datetime(df["order_date"],errors = 'coerce')
df['sales_amount']= pd.to_numeric(df['sales_amount'],errors ='coerce')

print("Order Date:",df["order_date"])
print('Ship Date:',df["sales_amount"])


# =========================================================================
# Task 1 --- Extract moths from order date
# =========================================================================

df['month']= df["order_date"].dt.to_period('M')
print(" Months Data:")
print(df[['order_date','month']].head())



# ============================================================================
# Task 2  Calculate Monthly Sales
# ==========================================================================

monthly_sales = df.groupby('month')['sales_amount'].sum()

print("Monthly Sales:")
print(monthly_sales)



#=============================================================================
# # Task 3 ----- Plot monthlu sales Trends
# ============================================================================

plt.figure(figsize=(8,5))
plt.boxplot(monthly_sales.sort_values(ascending= False))  #kind='line',marker= 'o',color='blue'))
plt.title("Monthly Sales Trend\n")
plt.xlabel('Month')
plt.ylabel("Total Sales")
plt.grid(True)
plt.show()
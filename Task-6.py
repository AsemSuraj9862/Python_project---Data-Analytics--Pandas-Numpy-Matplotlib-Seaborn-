import pandas as pd
import numpy as np

# *******************************  Customer analysis ********************************

# Task
# Indetify top customers by purchase amount.
# Calculate average spending per customer.
## Identify repet cusomers.

# Skills practiced
# --- Customers segmentations
# --- Aggregations


# Load Data

df = pd.read_csv("sales_dataset-2_cleaned.csv")
print("Cleaned Original Data:",df)

# Clean columns names

df.columns = df.columns.str.strip().str.lower()
print("Clean columns names:",df.columns)


# convert datatype  sales_amount to numeric

df['sales_amount'] = pd.to_numeric(df["sales_amount"],errors= 'coerce')
print("Convert datatype sales_amount to numeric:",df["sales_amount"])


# ============================================================
# Task 1 ------ Identified to customers by purchase Amount
# ============================================================

sales_customers = df.groupby('customer_name')['sales_amount'].sum()
top_customers = sales_customers.sort_values(ascending = False).head(10)

print("Top Customers By Purchase Amount:",top_customers)


# ============================================================
# Task 2 -----  Calculate Average spending per customers
# ============================================================

average_spending = df.groupby('customer_name')['sales_amount'].mean()
print("Average spending per customers:")
print(average_spending.head(10))



# ============================================================
# Task 3 ---- Identified repeat customers
# ============================================================


customer_orders = df.groupby('customer_name').size()
print("customer_orders",customer_orders)

print("Repeated Customers:")

print("No to Repeated customers:",len(customer_orders))




# ================================== Complete Task 6 =====================================



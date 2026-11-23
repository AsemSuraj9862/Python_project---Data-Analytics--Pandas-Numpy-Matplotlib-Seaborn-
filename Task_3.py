import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==================================================================
# Task 3 Sales perfomance analysis
# ==================================================================
# =====TASK ===

# Calculate total sales revenue
# Calculate total profit
# find average order value
# identify highest and lowest sales

# Skills practiced
# -- Aggresgation
# -- Descritive 
# ===============================================================

# Task1 
# Load Data

df = pd.read_csv("sales_dataset-2_cleaned.csv")
print("Original clean dataset:",df
)

# clean columns
df.columns = df.columns.str.strip().str.lower()
print("Clean columns in dataset:",df.columns)

# convert columns to numeric if necessary

df['sales_amount'] = pd.to_numeric(df['sales_amount'],errors = 'coerce')
df['profit_amount'] =pd.to_numeric(df['profit_amount'],errors ='coerce')


# === Task1 === Calculate total sales revenue ==================================

total_sales = df['sales_amount'].sum()
print("Total Sales revenue :\n",total_sales)

# ===============================================================================

# Task 2 ======== Calculate total profit ========================================

total_profit = df['profit_amount'].sum()
print("Total profit amount:\n",total_profit)

# Task 3 =======  Find average order value. ======================================

average_order_value = df['sales_amount'].mean()
print("Average _order_value for sales_amount:\n",average_order_value)


# Task 4 === Highest and lowest sales  ===========================================

highest_sales = df['sales_amount'].max()
lowest_sales = df['sales_amount'].min()

print("Highest Sales Amount:\n",highest_sales)
print('Lowest Sales Amount:\n',lowest_sales)

# ================================================================================
# Additional Descritive sales
# ================================================================================

print("Additional Descritive Sales:")
print(df['sales_amount'].describe()) 

# ==================================================================================
# Identity rows with highest and lowest sales
# ================================================================================

print("\n order with the highest sales:")
print(df.loc[df['sales_amount'].idxmax()])

print("\n order with lowest sales:")
print(df.loc[df['sales_amount'].idxmin()])  


# df['sales-_amount']  means ----- select the sales_amount columns
# df['sales_amount'].idxmax() --- Find the index of the rows with the maximum sales_amount
# df['sales_amount'].idxmin() --- Find the index of the rows with the minimum sales_amount
# df.loc[...] ------------------- use that index to retrieve the entire row
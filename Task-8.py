import pandas as pd
import numpy as np




#  =============================== 8.--- Profitable Analysis =====================================

# Task 
# Calculate profit margin for each product
# Identified products with negative profit.
# Suggest reasons for loss.

# Skills Practided
# ---- Business Analytics 
# ---- Calcuated Columns


# Load Data

df = pd.read_csv("sales_dataset-2_cleaned.csv")
print("\nCleaned Dataset :",df)


# Clean columns names
df.columns = df.columns.str.strip().str.lower()
print("\nCleaned columns :",df.columns)


# Convert numeric columns

df['cost_amount'] = pd.to_numeric(df["cost_amount"],errors= 'coerce')
df['profit_amount']= pd.to_numeric(df["profit_amount"],errors='coerce')

print('Convert cost_amount into numeric columns\n ',df['cost_amount'])
print('Convert profit_amount into numeric columns\n',df['profit_amount'])


# ========================================================================
# Task 1 -------------- Calculate profit margin -----------------
# ========================================================================


# profit margin = Profit / cost * 100

df['profit_margin'] = (df['profit_amount'] / df['cost_amount']) * 100

print("\n Sample profit margin:")
print(df[['product_name','cost_amount','profit_amount']].head())


#
# -----------------------------------------
# Profit margin by product
# -----------------------------------------

product_profit_margin = df.groupby('product_name').agg({
    'sales_amount':'sum',
    'profit_amount':'sum'
})

product_profit_margin['profit_margin'] = (
    product_profit_margin['profit_amount'] /
    product_profit_margin['sales_amount']
) * 100

print("\nProfit Margin by Product:")
print(product_profit_margin)


# -----------------------------------------
# Task 2: Identify products with negative profit
# -----------------------------------------

loss_products = product_profit_margin[
    product_profit_margin['profit_amount'] < 0
]

print("\nProducts with Negative Profit:")
print(loss_products)

# -----------------------------------------
# Task 3: Suggest reasons for loss
# -----------------------------------------

print("\nPossible Reasons for Loss:")

print("1. High discount offered to customers")
print("2. High product cost or manufacturing cost")
print("3. Logistics or shipping expenses")
print("4. Seasonal clearance sales")
print("5. Pricing strategy issues")
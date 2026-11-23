

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Data

df = pd.read_csv("sales_dataset-2_cleaned.csv")
print("Original dataset after cleaning:",df)


# Clean columns names

df.columns = df.columns.str.strip().str.lower()
print("clean columms name:",df.columns)

# convert columns name into numeric if needed
# ['sales_amount'] and ['profit_amount']

df['sales_amount']= pd.to_numeric(df['sales_amount'],errors = 'coerce')
df['profit_amount']= pd.to_numeric(df['profit_amount'],errors= 'coerce')

print("convert columns name from sales_amount into numeric:",df['sales_amount'])
print("convert columns name from profit_amount into numeric:",df['profit_amount'])

# ==========================================
# task1
# ==========================================

product_sales= df.groupby("product_name")['sales_amount'].sum()
top_10_product = product_sales.sort_values(ascending = False).head(10)
print("Top Ten Product:",top_10_product)


# ============================================
# Task 2   ---- product with highest profit
# ============================================

profit_product = df.groupby('product_name')['profit_amount'].sum()
highest_profit_product = profit_product.sort_values(ascending = False).head(10)

print("Highest_profit_product:")
print(highest_profit_product)

# =============================================
# Task 3  --- product with low values
# =============================================

low_sales_product = product_sales.sort_values(ascending = True).head(10)
print("Low sales product:")
print(low_sales_product)

# =============================================
#  ----- Ranking product by revenue
# ============================================

product_ranking = product_sales.sort_values(ascending= False).reset_index()

product_ranking['rank'] = product_ranking['sales_amount'].rank(ascending = False ,method ='dense')

print("product Ranking Reveue:")
print(product_ranking.head(10))
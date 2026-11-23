

import pandas  as pd 
import numpy as np
import matplotlib.pyplot as plt



# Calculate total sales by region
# Identified best perfoming region
# Visualized region sales using bar char

# SKILLS PRACTICE
# ----- grouping
# ----- Visualized and Business Analysis




# load Data

df = pd.read_csv("sales_dataset-2.csv")
print("Original Data:",df)

# convert column name

df.columns = df.columns.str.strip().str.lower()
print("Correct data type or convert columns names:",df.columns)


# convert datatype
# 

df['sales_amount'] = pd.to_numeric(df["sales_amount"],errors ='coerce')
print("\n Convert datatype into numeric:",df["sales_amount"])




# ==================================================
# Task 1  ----- Calculate Total sales region
# ==================================================

sales_region = df.groupby('region')['sales_amount'].sum()
print("\n Total sales amount:")
print(sales_region)


# ===================================================
# Task 2 Identified best performing region
# ===================================================

best_performing_region = sales_region.idxmax()
best_sales =   sales_region.max()
top_10_best_sales = sales_region.head(10)

print("\nBest performing sales_region:", best_performing_region)
print("\nHighest_Sales =",best_sales)
print("Top 10 highest sales =",top_10_best_sales)




# =====================================================
#  Task 3 -----Visualized region sales using bar char
# =====================================================


plt.figure(figsize=(8,5))
plt.boxplot(sales_region.sort_values(ascending= False))  #.plot(kind="bar"),color='skyblue')
plt.title("Regional sales Performance\n")
plt.xlabel("Region")
plt.ylabel("Sales region")
plt.grid()
plt.show()

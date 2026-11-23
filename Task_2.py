
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load Data 

df = pd.read_csv("sales_dataset-2_cleaned.csv")
print("Clean dataset after cleaning:",df)

print("Head:\n",df.head())
print("info:\n",df.info())
print("shape:",df.shape)

# Clean columns name

df.columns = df.columns.str.strip().str.lower()
print("clean columns name:",df.columns.tolist())

# =================================================================================
# check if  sales_amount columns exits
if 'sales_amount' not in df.columns:
    print("\n Error: Sales amount columns not found in sales dataset.")
    print("Available columns are:")
    print(df.columns.tolist())

else:
    # convert to numeric if needed
    df['sales_amount']= pd.to_numeric(df["sales_amount"],errors= 'coerce')


# Remove missing values for sales amount
sales_data = df['sales_amount'].dropna()
print("sales_data:\n",sales_data)

#===================================================================================
# Identified outlier using IQR method
Q1 = sales_data.quantile(0.25)
Q3 = sales_data.quantile(0.75)

IQR= Q3 -Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

print("\n IQR method result:")
print("\n Q1",Q1)
print("\n Q3",Q3)
print("\n Lower_limit:",lower_limit)
print("\n upper_limit:",upper_limit)

# =================================================================================

# Detection Outlier

outlier_iqr = df[(df["sales_amount"] < lower_limit) | (df["sales_amount"] > upper_limit)]
print("Detection outlier:",outlier_iqr)

print("\n No of outlier detection:",len(outlier_iqr))
print("\n Sample outlier:")
print(outlier_iqr[['sales_amount']].head())


# =================================================================================
# Task 2 
# Box plot
# =================================================================================

plt.figure(figsize=(8,5))
plt.boxplot(sales_data)
plt.title("Boxplot of sales amount")
plt.ylabel("Sales_Amount")
plt.grid(True)
plt.show()

# =============================================================================
# Compare result
# =============================================================================

# Remove outlier

df_no_outlier = df[(df["sales_amount"] >= lower_limit) & (df["sales_amount"] <= upper_limit)]

print("Rows before outlier:",len(df))
print("rows after removing outlier:",len(df_no_outlier))



# Save result

outlier_iqr.to_csv(
"C:/Users/This PC/Documents/PYTHON PROJECT/Data-Analytics_practice/sales_outlier.csv",
index= False
)

df_no_outlier.to_csv(
    "C:/Users\This PC/Documents/PYTHON PROJECT/Data-Analytics_practice/sales_dataset_without_outlier.csv",
    index = False
)
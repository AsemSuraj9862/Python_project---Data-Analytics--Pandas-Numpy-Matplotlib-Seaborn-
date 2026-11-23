#=======================================
# 9. Correlation Analysis 
# Understand relationships between numerical variables. 
# Tasks 
# • Calculate correlation matrix. 
# • Identify relationships between: 
# o Quantity 
# o Sales 
# o Profit 
# • Visualize correlation heatmap. 
# Skills Practiced 
# • Correlation 
# • Heatmap visualization
#=======================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset
df = pd.read_csv("sales_dataset-2_cleaned.csv")
print("Clean dataset after cleaning:",df)



# Clean column names
df.columns = df.columns.str.strip().str.lower()

print("Columns in dataset:")
print(df.columns)

# Convert numeric columns
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['sales_amount'] = pd.to_numeric(df['sales_amount'], errors='coerce')
df['profit_amount'] = pd.to_numeric(df['profit_amount'], errors='coerce')

# ------------------------------------------
# Task 1: Calculate correlation matrix
# ------------------------------------------

corr_matrix = df[['quantity', 'sales_amount', 'profit_amount']].corr()

print("\nCorrelation Matrix:")
print(corr_matrix)

# ------------------------------------------
# Task 2: Identify relationships
# ------------------------------------------

print("\nRelationship Insights:")
print("Quantity vs Sales:", corr_matrix.loc['quantity', 'sales_amount'])
print("Quantity vs Profit:", corr_matrix.loc['quantity', 'profit_amount'])
print("Sales vs Profit:", corr_matrix.loc['sales_amount', 'profit_amount'])

# ------------------------------------------
# Task 3: Visualize correlation heatmap
# ------------------------------------------

plt.figure(figsize=(6,4))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap='coolwarm',
    linewidths=0.5
)

plt.title("Correlation Heatmap")
plt.show()
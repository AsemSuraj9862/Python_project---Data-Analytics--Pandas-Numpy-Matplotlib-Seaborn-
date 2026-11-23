print("============================= SALES DATA ANALYSIS ===============================")

import pandas as pd
import numpy as np

# =====================================================================
#1 File Paths
# =====================================================================

input_file = 'sales_dataset-2.csv'
output_file = 'sales_dataset-2_cleaned.csv'

# =====================================================================
#2 Load dataset

df = pd.read_csv(input_file)   # loading file
print("original Data:",df)
print(df.head())
print(df.tail())

# ======================================================================
# Clean column name
#=======================================================================

df.columns = df.columns.str.strip().str.lower()
print("Clean column names:",df.columns)

# ========================================================================
# Convert blank values into NaN
# =======================================================================

df = df.replace(r'^\s*$',np.nan,regex= True)  # if blank in data       # r'^\s*$' regular expression
print(" convert missing value in Nan:",df)


# ========================================================================
# Task 1 Check missing values
#==========================================================================

print("Missing values before cleaning:")
print(df.isnull().sum())

# ===========================================================================
# Handle Missing values
# ===========================================================================
# Convert date columns

if 'order_date' in df.columns:
    df['order_date'] = pd.to_datetime(df['order_date'],
        errors = 'coerce',
        dayfirst = True

    )

if'ship_date' in df.columns:
    df['ship_date'] = pd.to_datetime(df['ship_date'],
          errors = 'coerce',
          dayfirst= True
    )

# ==================================================================================
# Filled numeric_columns with means
# ==================================================================================

numeric_columns = df.select_dtypes(include='number').columns
for col in numeric_columns:
    df[col] = df[col].fillna(df[col].mean())



# ================================================================================
# filled text_columns with mode
# =================================================================================

text_columns = df.select_dtypes(include='object').columns
for col in text_columns:
    if not df[col].mode().empty:
        df[col]= df[col].fillna(df[col].mode()[0])

# ====================================================================================
# fill date_columns with mode
# ===================================================================================

date_columns = df.select_dtypes(include= 'datetime').columns

for col in date_columns:
    if not df[col].mode().empty:
        df[col]= df[col].fillna(df[col].mode()[0])



print("\n Missing values after cleaning:")
print(df.isnull().sum())


# ================================================================================= 
# # task 3remove duplicate values
#===================================================================================


print("\n Rows befor removing duplicates:",len(df))

print("Duplicates rows:",df.duplicated().sum())

print("Rows after removing duplicates:",len(df))


# =======================================================================
# Task 4 Convert data types
#                               ID columns should be string
# =======================================================================

id_columns = [
    'order_id',
    'invoice_id',
    'customer_id'
]

for col in id_columns:
    if col  in df.columns:
        df[col]= df[col].astype('string')


# =========================================================================
# convert select columns to category
# =========================================================================

category_columns = [
    'customer_name',
    'segment',
    'city',
    'state',
    'product_category',
    'sub_category',
    'sales_channel',
    'payment_method',
    'returned',
    'sales_rep',
    'order-priority'
]

for col in category_columns:
    if col in df.columns:
        df[col]= df[col].astype('category')



#============================================================================
# diaplay data type
#===========================================================================

print("\n Final data type:")
print(df.dtypes)

# ================================================================================
# Save Data
# ====================================================================================

df.to_csv(output_file,index = False)
print("\n Cleaned dataset saved successful:",output_file)

"""
=========================================================
Project Title : Sales Data Analysis
Week          : Week 3 - Introduction to Data Analysis
Author        : Bammidi Ramya Jyothi

Description:
This project analyzes a sales dataset using the Pandas
library. It loads the dataset, performs data cleaning,
calculates business metrics, and generates a formatted
sales report.
=========================================================
"""

# Import the pandas library
import pandas as pd

# -------------------------------------------------------
# STEP 1: LOAD THE DATASET
# -------------------------------------------------------

print("=" * 60)
print("            SALES DATA ANALYSIS PROJECT")
print("=" * 60)

try:
    # Read the CSV file
    df = pd.read_csv("sales_data.csv")
    print("\n Dataset loaded successfully!\n")

except FileNotFoundError:
    print("Error: sales_data.csv not found.")
    exit()

# -------------------------------------------------------
# STEP 2: EXPLORE THE DATASET
# -------------------------------------------------------

print("=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)

print("\nFirst Five Rows")
print(df.head())

print("\nDataset Shape")
print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

print("\nColumn Names")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

# -------------------------------------------------------
# STEP 3: CHECK MISSING VALUES
# -------------------------------------------------------

print("\n" + "=" * 60)
print("CHECKING MISSING VALUES")
print("=" * 60)

print(df.isnull().sum())

# Fill missing numeric values with mean
numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns

for column in numeric_columns:
    if df[column].isnull().sum() > 0:
        df[column].fillna(df[column].mean(), inplace=True)

# Fill missing text values with "Unknown"
object_columns = df.select_dtypes(include=["object"]).columns

for column in object_columns:
    if df[column].isnull().sum() > 0:
        df[column].fillna("Unknown", inplace=True)

print("\nMissing values handled successfully.")

# -------------------------------------------------------
# STEP 4: REMOVE DUPLICATE ROWS
# -------------------------------------------------------

duplicates = df.duplicated().sum()

print("\nDuplicate Records Found :", duplicates)

df.drop_duplicates(inplace=True)

print("Duplicate rows removed successfully.")

# -------------------------------------------------------
# STEP 5: DESCRIPTIVE STATISTICS
# -------------------------------------------------------

print("\n" + "=" * 60)
print("DESCRIPTIVE STATISTICS")
print("=" * 60)

print(df.describe())

# -------------------------------------------------------
# STEP 6: SALES ANALYSIS
# -------------------------------------------------------

print("\n" + "=" * 60)
print("PERFORMING SALES ANALYSIS")
print("=" * 60)

# Total Revenue
total_revenue = df["Total_Sales"].sum()

# Average Sale
average_sale = df["Total_Sales"].mean()

# Highest Sale
highest_sale = df["Total_Sales"].max()

# Lowest Sale
lowest_sale = df["Total_Sales"].min()

# Total Quantity Sold
total_quantity = df["Quantity"].sum()

# Average Quantity
average_quantity = df["Quantity"].mean()

# Product-wise Sales
product_sales = df.groupby("Product")["Total_Sales"].sum()

best_product = product_sales.idxmax()
best_product_sales = product_sales.max()

# Region-wise Sales
region_sales = df.groupby("Region")["Total_Sales"].sum()

best_region = region_sales.idxmax()

# Customer-wise Sales
customer_sales = df.groupby("Customer_ID")["Total_Sales"].sum()

top_customer = customer_sales.idxmax()
top_customer_sales = customer_sales.max()

# -------------------------------------------------------
# STEP 7: DISPLAY REPORT
# -------------------------------------------------------

print("\n")
print("=" * 60)
print("               SALES ANALYSIS REPORT")
print("=" * 60)

print(f"Total Revenue           : ₹ {total_revenue:,.2f}")
print(f"Average Sale            : ₹ {average_sale:,.2f}")
print(f"Highest Sale            : ₹ {highest_sale:,.2f}")
print(f"Lowest Sale             : ₹ {lowest_sale:,.2f}")

print()

print(f"Total Quantity Sold     : {total_quantity}")
print(f"Average Quantity Sold   : {average_quantity:.2f}")

print()

print(f"Best Selling Product    : {best_product}")
print(f"Product Revenue         : ₹ {best_product_sales:,.2f}")

print()

print(f"Best Performing Region  : {best_region}")

print()

print(f"Top Customer            : {top_customer}")
print(f"Customer Purchase       : ₹ {top_customer_sales:,.2f}")

print("=" * 60)

# -------------------------------------------------------
# STEP 8: SAVE REPORT
# -------------------------------------------------------

with open("output_report.txt", "w", encoding="utf-8") as report:

    report.write("SALES DATA ANALYSIS REPORT\n")
    report.write("=" * 50 + "\n\n")

    report.write(f"Total Revenue           : ₹ {total_revenue:,.2f}\n")
    report.write(f"Average Sale            : ₹ {average_sale:,.2f}\n")
    report.write(f"Highest Sale            : ₹ {highest_sale:,.2f}\n")
    report.write(f"Lowest Sale             : ₹ {lowest_sale:,.2f}\n\n")

    report.write(f"Total Quantity Sold     : {total_quantity}\n")
    report.write(f"Average Quantity Sold   : {average_quantity:.2f}\n\n")

    report.write(f"Best Selling Product    : {best_product}\n")
    report.write(f"Product Revenue         : ₹ {best_product_sales:,.2f}\n\n")

    report.write(f"Best Performing Region  : {best_region}\n\n")

    report.write(f"Top Customer            : {top_customer}\n")
    report.write(f"Customer Purchase       : ₹ {top_customer_sales:,.2f}\n")

print("\nReport generated successfully.")
print("Report saved as 'output_report.txt'")

print("\nProject completed successfully!")

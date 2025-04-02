# coffe sales from year 2024 to present
import numpy as np
import pandas as pd
import os

# File paths
file1 = "C:/Users/Administrator/OneDrive/Desktop/Projects/sales/coffee/index_1.csv"
file2 = "C:/Users/Administrator/OneDrive/Desktop/Projects/sales/coffee/index_2.csv"

# Load datasets
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Inspect datasets
print("Dataset 1 Shape:", df1.shape)
print("Dataset 2 Shape:", df2.shape)

# Check common columns
print("Columns in Dataset 1:", df1.columns)
print("Columns in Dataset 2:", df2.columns)

# Add missing 'card' column in df2 (fill with 'No Card' or NaN)
df2["card"] = "No Card" 

# Concatenate both datasets
df = pd.concat([df1, df2], ignore_index=True)

# Convert date column (if available) to datetime format
if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"])

# Add 'Year' column for better tracking
df["Year"] = df["date"].dt.year

# Handle missing values (forward fill)
df.ffill(inplace=True)  # Fixed the deprecated fillna() warning

# Remove duplicates
df.drop_duplicates(inplace=True)

# ✅ Ensure the 'data/' directory exists before saving
output_dir = "C:/Users/Administrator/OneDrive/Desktop/Projects/sales/coffee/data"
os.makedirs(output_dir, exist_ok=True)

# Save cleaned data
output_file = os.path.join(output_dir, "cleaned_coffee_sales.csv")
df.to_csv(output_file, index=False)

print(f" Data cleaning complete! Cleaned file saved as '{output_file}'.")

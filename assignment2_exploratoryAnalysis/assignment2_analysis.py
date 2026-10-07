import pandas as pd
df = pd.read_csv("data/Sales-Export_2019-2020.csv", thousands=",")
df.columns = df.columns.str.strip()

print("DataFrame Shape:")
print(df.shape) 
print("\n")

print("DataFrame Data Types:")
print(df.dtypes)
print("\n")

print("First 5 Rows:")
print(df.head())
print("\n")

print("Missing Values:")
print(df.isnull().sum())
print("\n")

print("Calculates descriptive statistics for the 'order_value_EUR' and 'cost' columns:")
print(df["order_value_EUR"].describe())
print("Median of order_value_EUR:", df["order_value_EUR"].median())
print(df["cost"].describe())
print("Median of cost:", df["cost"].median())
print("\n")

print("Average Order Value by Category:")
print(df.groupby("category")["order_value_EUR"].mean())
print("\n")

print("Highest and Lowest Order Values:")
highest_row = df["order_value_EUR"].idxmax()
lowest_row = df["order_value_EUR"].idxmin()
print("Highest order value:", df["order_value_EUR"].max())
print(df.loc[highest_row])
print("\n")
print("Lowest order value:", df["order_value_EUR"].min())
print(df.loc[lowest_row])




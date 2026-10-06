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

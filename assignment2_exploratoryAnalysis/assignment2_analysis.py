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

highest_row = df["order_value_EUR"].idxmax()
lowest_row = df["order_value_EUR"].idxmin()
print("Highest order value:", df["order_value_EUR"].max())
print(df.loc[highest_row])
print("\n")
print("Lowest order value:", df["order_value_EUR"].min())
print(df.loc[lowest_row])
print("\n")

avg_order = df["order_value_EUR"].mean()
threshold = 105000
if avg_order >= threshold:
    print("The average order value meets the threshold.")
else:
    print("The average order value is below the threshold.")
print("\n")   

print("Summary of Findings:")
print("The dataset contains 1000 orders from 2019 to 2020, with no missing values.")
print("The average order value is 113,361 EUR, and the median is 105,419 EUR.")
print("The standard deviation of order values is 61,775 EUR, indicating moderate variation in order sizes.")
print("Accessories has the highest average order value (134,398 EUR) among all categories.")
print("The highest order value is 383,996.76 EUR, and the lowest is 15,100.57 EUR.")
print("The average order value exceeds the 105,000 EUR threshold, indicating healthy order performance.")


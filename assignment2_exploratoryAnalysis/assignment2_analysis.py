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
print("The dataset contains 1000 orders from 2019 to 2020, and none of the columns have missing values, so the data is pretty clean.")
print("On average, each order is worth about 113,361 EUR, with a median of 105,419 EUR.")
print("The standard deviation is quite large which is 61,775 EUR, meaning order sizes vary a lot across the dataset.")
print("Interestingly, Accessories stands out with the highest average order value, around 134,398 EUR per order.")
print("The largest single order reached 383,996.76 EUR, while the smallest was only 15,100.57 EUR.")
print("Overall, the average order value clears the 105,000 EUR threshold, so the business looks healthy.")

print("\nData for Recommendations:")
print("\n")
print(df.groupby("country")["order_value_EUR"].sum())
df["year"] = pd.to_datetime(df["date"], format="%m/%d/%Y").dt.year
yearly = df.groupby("year")["order_value_EUR"].agg(["count", "sum", "mean"])
print("\n")
print(yearly.round(0))
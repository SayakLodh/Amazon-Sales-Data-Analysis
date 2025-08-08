import pandas as pd
import numpy as np

df = pd.read_csv(r"D:\Amazon sales data\amazon.csv")
print(df.info())
print(df.describe())

# Clean and convert columns
df['discount_percentage'] = df['discount_percentage'].str.replace('%', '').astype(float)
df['rating'] = df['rating'].str.extract(r'(\d+\.\d+)').astype(float)

df['rating_count'] = df['rating_count'].str.replace(',', '', regex=False)
df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce')  # Converts invalid strings to NaN
df['rating_count'] = df['rating_count'].fillna(0)
df['rating_count'] = df['rating_count'].astype(int)
# Remove ₹ and commas, strip whitespace, then convert to float
df['discounted_price'] = df['discounted_price'].str.replace('₹', '', regex=False)
df['discounted_price'] = df['discounted_price'].str.replace(',', '', regex=False).str.strip().astype(float)

df['actual_price'] = df['actual_price'].str.replace('₹', '', regex=False)
df['actual_price'] = df['actual_price'].str.replace(',', '', regex=False).str.strip().astype(float)

df['profit'] = df['actual_price'] - df['discounted_price']
df['revenue'] = df['discounted_price'] * df['rating_count']
df['discount_amount'] = df['actual_price'] * (df['discount_percentage'] / 100)
df['sale_date'] = pd.to_datetime(np.random.choice(pd.date_range(start='2023-01-01', end='2023-12-31'), size=len(df)))

df.to_excel("cleanedamazon.xlsx", index=False)

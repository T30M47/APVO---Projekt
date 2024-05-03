import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a DataFrame
data = pd.read_csv('test.csv')
#data = pd.read_csv('retail_cleaned.csv')

# Group by product and sum the quantities sold
product_sales = data.groupby('Description')['Quantity'].sum()

# Sort the products by total quantity sold in descending order and get the top 50
top_50_products = product_sales.sort_values(ascending=False).head(300)
print("Number of unique products:", data['StockCode'].nunique())

# Plotting
plt.figure(figsize=(12, 8))
top_50_products.plot(kind='bar', color='skyblue')
plt.title('Top 50 Most Sold Products')
plt.xlabel('Product')
plt.ylabel('Total Quantity Sold')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

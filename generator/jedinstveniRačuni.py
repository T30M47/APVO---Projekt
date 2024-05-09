import pandas as pd

# Assuming your data is in a CSV file named 'invoices.csv'
data = pd.read_csv('generator/csv/retail_cleaned.csv')

# Count the number of unique invoice numbers
num_unique_invoices = data['InvoiceNo'].nunique()

print("Number of unique invoice numbers in the data:", num_unique_invoices)
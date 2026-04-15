import pyodbc
import pandas as pd

# 1. THE CONNECTION (One single line - no Enter keys used)
conn_str = r'Driver={SQL Server};Server=LAPTOP-SODOC3H3\SQLEXPRESS02;Database=AdventureWorks2019;Trusted_Connection=yes;'
conn = pyodbc.connect(conn_str)

# 2. THE QUERY (One single line)
query = "SELECT Name, ListPrice FROM Production.Product ORDER BY ListPrice DESC"

# 3. THE RESULT
df = pd.read_sql(query, conn)
print("--- DATA CONNECTED SUCCESSFULLY ---")
print(df.head(10))

# 4. THE TRANSFORMATION(Adding 20% VAT)
df['PriceWithVAT'] = df['ListPrice'] * 1.20

print("--- UK Inventory with 20% VAT ---")
print(df[['Name', 'ListPrice', 'PriceWithVAT']].head(10))

# 5. THE EXPORT (Save the data to a new CSV file you can open in Excel)
df.to_csv('Luxury_Bike_Report.csv', index=False)

print("---FILE SAVED: Check your folder for Luxury_Bike_Report.csv ---")

# Close the connection
conn.close()
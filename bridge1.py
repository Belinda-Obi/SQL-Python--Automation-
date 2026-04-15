import pyodbc
import pandas as pd
import matplotlib.pyplot as plt

# 1. THE CONNECTION
conn_str = r'Driver={SQL Server};Server=LAPTOP-SODOC3H3\SQLEXPRESS02;Database=AdventureWorks2019;Trusted_Connection=yes;'
conn = pyodbc.connect(conn_str)

# 2. THE QUERY (Top 10 most expensive items)
query = "SELECT TOP 10 Name, ListPrice FROM Production.Product ORDER BY ListPrice DESC"

# 3. DATA EXTRACTION & MATH
df = pd.read_sql(query, conn)
df['PriceWithVAT'] = df['ListPrice'] * 1.20

# 4. THE VISUALIZATION (Creating a Bar Chart)
# This creates a chart showing the Name on the bottom and Price on the side
df.plot(kind='bar', x='Name', y='ListPrice', color='skyblue', figsize=(10, 6))

plt.title('Top 10 Most Expensive Luxury Bikes')
plt.ylabel('Price ($)')
plt.xticks(rotation=45, ha='right') # Tilts the names so they don't overlap
plt.tight_layout() # Makes sure everything fits in the picture

# 5. SAVE THE CHART
plt.savefig('Bike_Price_Visualization.png')
df.to_csv('Luxury_Bike_Report.csv', index=False)

print("--- SUCCESS: Report Saved and Chart Generated! ---")
conn.close()
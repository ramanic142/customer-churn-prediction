import pandas as pd
import sqlite3
import os

# Define paths
data_path = os.path.join("Data", "WA_Fn-UseC_-Telco-Customer-Churn.csv")
db_path = os.path.join("Data", "churn.db")

# Step 1: Load CSV into a pandas DataFrame
df = pd.read_csv(data_path)

print("Data loaded successfully!")
print("Shape of dataset (rows, columns):", df.shape)
print("\nFirst 5 rows:")
print(df.head())

# Step 2: Create a SQLite database and load data into it
conn = sqlite3.connect(db_path)
df.to_sql("customers", conn, if_exists="replace", index=False)
conn.close()

print(f"\nData successfully loaded into SQLite database at: {db_path}")

# Step 3: Verify by querying the database with SQL
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM customers")
total_rows = cursor.fetchone()[0]
print(f"\nTotal rows in database: {total_rows}")

cursor.execute("SELECT Churn, COUNT(*) FROM customers GROUP BY Churn")
churn_counts = cursor.fetchall()
print("Churn distribution:")
for row in churn_counts:
    print(f"  {row[0]}: {row[1]}")

conn.close()
import pandas as pd
import mysql.connector

# Read CSV file
df = pd.read_csv("data/history_processed.csv")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="browser_ai"
)

cursor = conn.cursor()

# Insert rows one by one
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO history_data
        (id, url, title, visit_count, last_visit_time, visit_time, category)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        int(row["id"]),
        str(row["url"]),
        str(row["title"]),
        int(row["visit_count"]),
        str(row["last_visit_time"]),
        str(row["visit_time"]),
        str(row["category"])
    ))

# Save changes
conn.commit()

print("Data imported successfully!")

# Close connection
cursor.close()
conn.close()
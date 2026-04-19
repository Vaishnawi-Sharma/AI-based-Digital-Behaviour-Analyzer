import shutil
import sqlite3
from analyzer import classify
import pandas as pd

# copying browsing data 
src = r"C:\Users\bhard\AppData\Local\Google\Chrome\User Data\Profile 3\History"
dst = r"data\History_copy"

try:
    shutil.copy2(src, dst)
    print("History file copied")
except Exception as e:
    print("Copy failed:", e)

print("History file copied")


# connection building 

conn = sqlite3.connect(r"data\History_copy")

query = """
SELECT
    u.id,
    u.url,
    u.title,
    u.visit_count,
    u.last_visit_time,
    v.visit_time
FROM urls u
JOIN visits v ON u.id = v.url
ORDER BY v.visit_time DESC
LIMIT 50
"""

# Read history
df = pd.read_sql_query(query, conn)

# clean history 
bad_titles = ["Error Page", "Redirecting...", "Home Page", "Welcome"]

df = df[~df["title"].isin(bad_titles)]
df = df[df["title"].notna()]
df = df[df["title"] != ""]
df = df.drop_duplicates(subset=["title","visit_time"])
drop_titles = ["Home", "Next Step", "Login", "Welcome"]

# time conversion into IST 
df["visit_time"] = pd.to_datetime(
    df["visit_time"] - 11644473600000000,
    unit="us",
    utc=True
).dt.tz_convert("Asia/Kolkata")

df["last_visit_time"] = pd.to_datetime(
    df["last_visit_time"] - 11644473600000000,
    unit="us",
    utc=True
).dt.tz_convert("Asia/Kolkata")

# time display modification 
df["visit_time"] = df["visit_time"].dt.strftime("%d-%m-%Y %I:%M:%S %p")
df["last_visit_time"] = df["last_visit_time"].dt.strftime("%d-%m-%Y %I:%M:%S %p")



# classify 

df["category"] = df.apply(
    lambda row: classify(row["title"], row["url"]),
    axis=1
)

# see result
print(df[["title","category","visit_time"]].head(20).to_string(index=False))

# Saving results to csv 
df.to_csv("data/history_processed.csv", index=False)
print("CSV saved")
conn.close()
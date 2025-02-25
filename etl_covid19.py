import sqlite3
import pandas as pd
import json

# ✅ Connect to SQLite Database
conn = sqlite3.connect("covid19.db")

# ✅ Read Data into Pandas DataFrame
df = pd.read_sql("SELECT * FROM covid_stats", conn)

# ✅ Convert `countryInfo` JSON string back to a dictionary
df["countryInfo"] = df["countryInfo"].apply(json.loads)

# ✅ Close connection
conn.close()

# ✅ Print DataFrame
print(df[["country", "countryInfo"]])

# ✅ Access specific values
print(df["countryInfo"][0]["iso2"])  # Output: 'IN'

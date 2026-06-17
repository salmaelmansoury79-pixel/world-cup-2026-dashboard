from supabase import create_client
import pandas as pd

# 1. Setup Connection
URL = "https://ljhxfuwzczwkqmnvksic.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxqaHhmdXd6Y3p3a3FtbnZrc2ljIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODE2OTUwNTMsImV4cCI6MjA5NzI3MTA1M30.7-4gPIWPBNsgyBYvOmCtVnjOvwEdJ5NtF2T_g2Qy5M4" # Your Token

supabase = create_client(URL, KEY)

# 2. Load the cleaned CSV
df = pd.read_csv("world_cup_cleaned.csv")

# 3. Rename columns to lowercase to match Supabase SQL schema
df.columns = df.columns.str.lower()

# Rename specific column to match 'match_date' in your SQL table
df = df.rename(columns={'date': 'match_date'})

# 4. Send data to Supabase
data = df.to_dict(orient="records")

try:
    response = supabase.table("matches").insert(data).execute()
    print("✅ Data successfully uploaded to Supabase!")
except Exception as e:
    print(f"❌ Error uploading data: {e}")
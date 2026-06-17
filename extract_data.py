import requests
import pandas as pd

# 1. API Configuration
# Storing the API token and the URL for the World Cup (WC) matches
API_TOKEN = "5bd869ecafbe49409edcd38ee34093b6"
URL = "https://api.football-data.org/v4/competitions/WC/matches"

# Setting up the required authorization header
headers = {
    "X-Auth-Token": API_TOKEN
}

print("🔄 Connecting to API and fetching World Cup data...")

# 2. HTTP Request
# Sending a GET request to the football-data API
response = requests.get(URL, headers=headers)

# Checking if the request was successful (HTTP Status 200)
if response.status_code == 200:
    data = response.json()
    matches = data.get("matches", [])
    
    print(f"✅ Successfully fetched {len(matches)} matches!")
    
    # 3. Data Extraction & Parsing
    # Loop through the JSON response and extract only the relevant fields
    extracted_matches = []
    for match in matches:
        extracted_matches.append({
            "Match_ID": match.get("id"),
            "Date": match.get("utcDate"),
            "Status": match.get("status"),
            "Stage": match.get("stage"),
            "Home_Team": match.get("homeTeam", {}).get("name"),
            "Away_Team": match.get("awayTeam", {}).get("name"),
            "Home_Score": match.get("score", {}).get("fullTime", {}).get("home"),
            "Away_Score": match.get("score", {}).get("fullTime", {}).get("away")
        })
    
    # Convert the structured list into a Pandas DataFrame for easy manipulation
    df = pd.DataFrame(extracted_matches)
    
    # Preview the first 5 rows of the dataframe in the terminal
    print("\n📊 Sample of the extracted data:")
    print(df.head())
    
    # 4. Data Storage (Stage 1 Complete)
    # Save the raw data into a CSV file for the next pipeline steps
    df.to_csv("world_cup_raw.csv", index=False)
    print("\n💾 Data successfully saved to: world_cup_raw.csv")

else:
    # Error handling in case the API key is invalid or the server is down
    print(f"❌ Connection Error: {response.status_code}")
    print(response.text)
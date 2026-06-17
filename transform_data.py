import pandas as pd

# 1. Load the raw data
df = pd.read_csv("world_cup_raw.csv")

# 2. Data Cleaning
# Remove matches that haven't been played yet (where status is not 'FINISHED')
df = df[df['Status'] == 'FINISHED']

# Fill NaN scores with 0
df['Home_Score'] = df['Home_Score'].fillna(0).astype(int)
df['Away_Score'] = df['Away_Score'].fillna(0).astype(int)

# 3. Data Transformation (Adding logic)
# Create a 'Winner' column based on scores
def get_winner(row):
    if row['Home_Score'] > row['Away_Score']:
        return row['Home_Team']
    elif row['Away_Score'] > row['Home_Score']:
        return row['Away_Team']
    else:
        return "Draw"

df['Winner'] = df.apply(get_winner, axis=1)

# 4. Save the cleaned data
df.to_csv("world_cup_cleaned.csv", index=False)

print("✅ Data transformation complete! Saved to: world_cup_cleaned.csv")
print(df[['Home_Team', 'Away_Team', 'Home_Score', 'Away_Score', 'Winner']].head())
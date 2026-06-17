import streamlit as pd_st
import streamlit as st
from supabase import create_client
import pandas as pd
import plotly.express as px

# 1. Supabase Connection Configuration
URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]

supabase = create_client(URL, KEY)

# 2. Fetch Data from Cloud (Supabase)
@st.cache_data # This keeps data in cache for faster loading
def load_data_from_cloud():
    response = supabase.table("matches").select("*").execute()
    return pd.DataFrame(response.data)

df = load_data_from_cloud()

# 3. Streamlit UI Layout
st.set_page_config(page_title="World Cup 2026 Live Dashboard", layout="wide")
st.title("🏆 World Cup 2026 - Data Analytics Dashboard")
st.write("This dashboard fetches data in real-time from our Supabase Cloud Database.")

# --- Row 1: Key Metrics ---
st.subheader("📊 Tournament Quick Stats")
col1, col2, col3 = st.columns(3)

total_matches = len(df)
total_goals = df['home_score'].sum() + df['away_score'].sum()
played_matches = df[df['status'] == 'FINISHED'].shape[0]

col1.metric("Total Matches Tracked", total_matches)
col2.metric("Total Goals Scored", int(total_goals))
col3.metric("Completed Matches", played_matches)

st.markdown("---")

# --- Row 2: Visualizations ---
st.subheader("📈 Advanced Analytics")
left_col, right_col = st.columns(2)

with left_col:
    st.write("### Top Winning Teams")
    # Filter out draws to see actual winners
    winners_df = df[df['winner'] != 'Draw']
    winner_counts = winners_df['winner'].value_counts().reset_index()
    winner_counts.columns = ['Team', 'Wins']
    
    # Create interactive Bar Chart with Plotly
    fig_bar = px.bar(winner_counts, x='Team', y='Wins', color='Wins', title="Number of Wins per Country")
    st.plotly_chart(fig_bar, use_container_width=True)

with right_col:
    st.write("### Match Status Overview")
    status_counts = df['status'].value_counts().reset_index()
    status_counts.columns = ['Status', 'Count']
    
    # Create interactive Pie Chart
    fig_pie = px.pie(status_counts, values='Count', names='Status', title="Matches Distribution")
    st.plotly_chart(fig_pie, use_container_width=True)

# --- Row 3: Raw Data Table ---
st.subheader("📋 Live Database Records")
st.dataframe(df[['match_date', 'stage', 'home_team', 'away_team', 'home_score', 'away_score', 'winner', 'status']])
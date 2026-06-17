# 🏆 World Cup 2026 Live Dashboard

An End-to-End Data Engineering & Analytics project that tracks and visualizes World Cup 2026 match statistics in real-time.

## 🚀 Project Overview
This project builds a full ETL (Extract, Transform, Load) pipeline that fetches live football data, cleans it, stores it securely in a PostgreSQL cloud database, and displays it on an interactive web dashboard.

## 🛠️ Tech Stack
- **Backend/Language:** Python
- **Data Engineering:** Pandas (Data Transformation & Cleaning)
- **Cloud Database:** Supabase (PostgreSQL)
- **Frontend/Dashboard:** Streamlit & Plotly (Interactive Charts)

## 📂 Project Structure
- `extract_data.py` : Fetches raw match data from the Football API.
- `transform_data.py` : Cleans the data, handles missing values, and adds business logic (e.g., match winners).
- `load_to_supabase.py` : Automatically uploads the cleaned records to the Supabase cloud database.
- `dashboard.py` : The Streamlit application that pulls data from the cloud and visualizes it.
- `requirements.txt` : List of required Python libraries for deployment.

## 🔗 Live Demo
👉 [Insert your Streamlit Link Here after deployment]
import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np

# URL Data
DATA_URL = "https://raw.githubusercontent.com/atyn104/intern/refs/heads/main/project_data_data.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)
    return df

try:
    data = load_data()

# --- Displaying summary boxes ---
col1, col2, col3 = st.columns(3)

with col1:
    summary1 = f"""
    <div style='border: 2px solid #DDD; padding: 15px; border-radius: 5px; font-size: 18px; height: 100px;'>
        <b>Average Experience:</b> {avg_experience:.2f} Years
    </div>
    """
    st.markdown(summary1, unsafe_allow_html=True)

with col2:
    summary2 = f"""
    <div style='border: 2px solid #DDD; padding: 15px; border-radius: 5px; font-size: 18px; height: 100px;'>
        <b>Total Jobs:</b> {total_jobs} <br>
        <span style="font-size: 14px;">Remote: {remote_val} | Onsite: {onsite_val} | Hybrid: {hybrid_val}</span>
    </div>
    """
    st.markdown(summary2, unsafe_allow_html=True)

with col3:
    summary3 = f"""
    <div style='border: 2px solid #DDD; padding: 15px; border-radius: 5px; font-size: 18px; height: 100px;'>
        <b>Top Job Title:</b> {top_job}
    </div>
    """
    st.markdown(summary3, unsafe_allow_html=True)

st.markdown("    ")
st.markdown(f"""
- Purata pengalaman yang diperlukan dalam industri ini adalah **{avg_experience:.2f} tahun**.
- Sebanyak **{total_jobs} iklan pekerjaan** direkodkan. Daripada jumlah ini, sebanyak **{remote_val} adalah kerja dari rumah (Remote)**.
- Pekerjaan yang paling kerap dipasang adalah **{top_job}**.
""")

# Show raw data preview
st.markdown("---")
st.subheader("1. Raw Data Preview")
st.dataframe(df.head(), use_container_width=True)

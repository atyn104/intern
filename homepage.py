import streamlit as st
import pandas as pd
import plotly.express as px

# URL untuk fail data AI & DS Job Market
url = "https://raw.githubusercontent.com/atyn104/intern/refs/heads/main/project_data_data.csv"

# Set page configuration
st.set_page_config(
    page_title="AI & DS Job Market",
    layout="wide"
)

st.title("💼 AI & DS Job Market ")

st.markdown("""
This dataset contains job market information related to Data Science and Artificial Intelligence. It contains information such as job title, experience level, type of work (Remote/Onsite), and required skills such as Python, SQL, etc.
""")

st.markdown("---")

# Function to load data with caching
@st.cache_data
def load_data(data_url):
    try:
        df = pd.read_csv(data_url)
        return df
    except Exception as e:
        st.error(f"An error occurred while loading the file from the URL: {e}")
        return pd.DataFrame()

# Load data
df = load_data(url)

if df.empty:
    st.stop()

# --- KOMPUTASI DATA ---

# 1. Purata Pengalaman Kerja (Years of Experience)
avg_experience = data['years_experience'].mean()

# 2. Jumlah pekerjaan & pecahan remote
total_jobs = len(data)
remote_counts = df['remote_type'].value_counts().to_dict()
remote_val = remote_counts.get('Remote', 0)
onsite_val = remote_counts.get('Onsite', 0)
hybrid_val = remote_counts.get('Hybrid', 0)

# 3. Pekerjaan yang paling popular
top_job = data['job_title'].mode()[0]

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

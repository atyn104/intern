import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# URL for the data file
url = "https://raw.githubusercontent.com/atyn104/EC2024/refs/heads/main/Computer_Science_and_Engineering_data.csv"

# Set page configuration
st.set_page_config(
    page_title="Scientific Visualization",
    layout="wide"
)

st.title("🎓 Student Performance Metrics ")

st.markdown("""
The Student achievement Metrics dataset, which intends to examine the impact of demographics, socioeconomic status, participation in extracurricular activities, and study habits on academic achievement, includes data on academic and non-academic factors of University of Malaya students. This information is used to create a prediction model of student performance and pinpoint the variables that affect students' success or failure in postsecondary education.
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
Computer_Science_and_Engineering_df = load_data(url)

if Computer_Science_and_Engineering_df.empty:
    st.stop()

# Clean and convert 'HSC' and 'SSC' columns to numeric, handling errors or missing data
Computer_Science_and_Engineering_df['HSC'] = pd.to_numeric(Computer_Science_and_Engineering_df['HSC'], errors='coerce')
Computer_Science_and_Engineering_df['SSC'] = pd.to_numeric(Computer_Science_and_Engineering_df['SSC'], errors='coerce')

# Replace NaN values with the column mean (optional, can replace with 0 or other value)
Computer_Science_and_Engineering_df['HSC'].fillna(Computer_Science_and_Engineering_df['HSC'].mean(), inplace=True)
Computer_Science_and_Engineering_df['SSC'].fillna(Computer_Science_and_Engineering_df['SSC'].mean(), inplace=True)

# --- KOMPUTASI DATA YANG HILANG ---

# 2. KOMPUTASI: Hitung rata-rata HSC dan SSC
hsc_ssc_avg = (Computer_Science_and_Engineering_df['HSC'] + Computer_Science_and_Engineering_df['SSC']) / 2  # Menggabungkan nilai HSC dan SSC
average_hsc_ssc = hsc_ssc_avg.mean()

# Hitung distribusi gender (Asumsi nama kolom adalah 'Gender')
gender_distribution = Computer_Science_and_Engineering_df['Gender'].value_counts().to_dict()
male_count = gender_distribution.get('Male', 0)
female_count = gender_distribution.get('Female', 0)

# --- Displaying summary boxes ---
# Create 3 columns for a clean, organized summary box
col1, col2, col3 = st.columns(3)  # 3 columns for summary box

with col1:
    # Kira purata HSC dan SSC
    average_hsc_ssc = 4.56  # Asumsi nilai purata HSC dan SSC sudah dihitung
    
    # Gabungkan informasi dalam kotak dengan HTML
    purata_hsc_ssc_summary = f"""
    <div style='border: 2px solid #DDD; padding: 10px; font-size: 18px;'>
        <b>Average HSC and SSC:</b> {average_hsc_ssc:.2f}
    </div>
    """
    
    # Gunakan st.markdown untuk memaparkan dalam satu kotak dengan border
    st.markdown(purata_hsc_ssc_summary, unsafe_allow_html=True)
    
with col2:
    # Kira jumlah lelaki dan perempuan secara berasingan
    male_count = gender_distribution.get('Male', 0)
    female_count = gender_distribution.get('Female', 0)
    
    # Kira jumlah keseluruhan pelajar
    total_students = male_count + female_count
    
    # Gabungkan kedua-dua nilai dalam satu kotak dengan HTML
    gender_summary = f"""
    <div style='border: 2px solid #DDD; padding: 10px; font-size: 18px;'>
        <b>Total:</b> {male_count + female_count} 
        <span style="margin-left: 10px;"><b> M:</b> {male_count} | <b> F:</b> {female_count}</span>
    </div>
    """
    
    # Gunakan st.markdown untuk memaparkan dalam satu kotak dengan border yang seragam
    st.markdown(gender_summary, unsafe_allow_html=True)
    
with col3:
    # Kira purata GPA (Overall)
    max_gpa = Computer_Science_and_Engineering_df['Overall'].max()  # Menghitung purata GPA
    
    # Gabungkan informasi dalam kotak dengan HTML
    overall_gpa_summary = f"""
    <div style='border: 2px solid #DDD; padding: 10px; font-size: 18px;'>
        <b>Highest Overall CGPA:</b> {max_gpa:.2f}
    </div>
    """
    
    # Gunakan st.markdown untuk memaparkan dalam satu kotak dengan border yang seragam
    st.markdown(overall_gpa_summary, unsafe_allow_html=True)
    
st.markdown("    ")
st.markdown("""
    -The average HSC and SSC, which is 4.56, are displayed in the first summary box. 
     It demonstrates that pupils with the highest academic standing at both the primary and school levels are accepted into the computer science and engineering department.
     The total number of students in the computer science and engineering department is displayed in the second summary box.  There are around 302 more male students than female students, who make up just about 141.
     The final summary box displays the highest CGPA of 4.00 that students received overall, demonstrating that this department is capable of achieving complete academic achievement.
     """)

# Show raw data preview
st.markdown("---")
st.subheader("1. Raw Data Preview")
st.dataframe(Computer_Science_and_Engineering_df.head(), use_container_width=True)


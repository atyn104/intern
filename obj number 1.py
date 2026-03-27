import streamlit as st
import pandas as pd
import plotly.express as px

# Konfigurasi halaman
st.title("📊 Objective 1: Skills Needs Analysis")
st.markdown("""
This page analyzes the most in-demand technical skill combinations by job title and experience level.
""")

# Load data
DATA_URL = "https://raw.githubusercontent.com/atyn104/intern/refs/heads/main/project_data_data.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_URL)

df = load_data()

# Senarai kolum kemahiran
skill_cols = ['skills_python', 'skills_sql', 'skills_ml', 'skills_deep_learning', 'skills_cloud']

# ==========================================
# VISUALIZATION 1: Popular Skills Bar Chart
# ==========================================
st.subheader("1. Most In-Demand Technical Skills (Overall)")

# Kira jumlah setiap kemahiran
df_skills = df[skill_cols].sum().reset_index()
df_skills.columns = ['Skill', 'Count']
df_skills['Skill'] = df_skills['Skill'].str.replace('skills_', '').str.title()
df_skills = df_skills.sort_values(by='Count', ascending=False)

fig1 = px.bar(
    df_skills, 
    x='Skill', 
    y='Count', 
    text_auto=True,
    color='Skill',
    color_discrete_sequence=px.colors.qualitative.Set2,
    title="Total Demand by Skill"
)
st.plotly_chart(fig1, use_container_width=True)


# ==========================================
# VISUALIZATION 2: Filterable Heatmap (Skills vs Position)
# ==========================================
st.markdown("---")
st.subheader("2. Analysis of Skill Requirements by Job Position")

# Group data mengikut tajuk kerja dan jumlahkan kemahiran
df_heatmap = df.groupby('job_title')[skill_cols].sum()

# Tukar nama kolum supaya nampak kemas
df_heatmap.columns = [col.replace('skills_', '').title() for col in df_heatmap.columns]

fig2 = px.imshow(
    df_heatmap,
    labels=dict(x="Skills", y="Job Title", color="Number of Jobs"),
    x=df_heatmap.columns,
    y=df_heatmap.index,
    color_continuous_scale='Viridis',
    aspect="auto",
    title="Heatmap: Job Title & Skills Relationship"
)
st.plotly_chart(fig2, use_container_width=True)


# ==========================================
# VISUALIZATION 3: Skills by Entry vs Senior (Interactive Filter)
# ==========================================
st.markdown("---")
st.subheader("3. Skills Based on Experience Level (Entry vs Mid vs Senior)")

# Guna multiselect filter untuk pengguna pilih tahap pengalaman
selected_exp = st.multiselect(
    "Select Experience Level:", 
    options=df['experience_level'].unique(), 
    default=df['experience_level'].unique()
)

# Filter dataframe mengikut pilihan
df_filtered = df[df['experience_level'].isin(selected_exp)]

# Penyusunan data (Melt data untuk grouped bar chart)
df_melted = df_filtered.melt(
    id_vars=['experience_level'], 
    value_vars=skill_cols, 
    var_name='Skill', 
    value_name='Required'
)
df_melted = df_melted[df_melted['Required'] == 1] # Ambil yang bernilai 1 sahaja (Ya, kemahiran diperlukan)

# Group dan kira jumlah
df_grouped = df_melted.groupby(['experience_level', 'Skill']).size().reset_index(name='Count')
df_grouped['Skill'] = df_grouped['Skill'].str.replace('skills_', '').str.title()

fig3 = px.bar(
    df_grouped,
    x='Skill',
    y='Count',
    color='experience_level',
    barmode='group',
    title="Comparison of Skill Requirements by Experience Level",
    labels={'experience_level': 'Experience Level', 'Count': 'Number of Job Advertisements'}
)
st.plotly_chart(fig3, use_container_width=True)

import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🏢 Objective 3: Remote Work Pattern & Adaptability")
st.markdown("""
This page assesses how **company size** and **industry type** influence flexible work policies (*Remote, Onsite, Hybrid*).
""")

# Load data
DATA_URL = "https://raw.githubusercontent.com/atyn104/intern/refs/heads/main/project_data_data.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_URL)

df = load_data()

# Buat Tab untuk kemas
tab1, tab2 = st.tabs(["📊 Analysis by Company Size", "🏭 Analysis by Industry"])

# ==========================================
# TAB 1: COMPANY SIZE VS REMOTE TYPE
# ==========================================
with tab1:
    st.subheader("1. Work Policies Based on Company Size")
    st.markdown("Do *Startups* offer more *Remote* opportunities than *Enterprises*?")

    # Agregat data mengikut saiz syarikat dan jenis kerja
    df_size_remote = df.groupby(['company_size', 'remote_type']).size().reset_index(name='count')

    # 100% Stacked Bar Chart
    fig_bar_size = px.bar(
        df_size_remote,
        x='count',
        y='company_size',
        color='remote_type',
        orientation='h',
        title="Breakdown of Job Types by Company Size",
        labels={'count': 'Number of Jobs', 'company_size': 'Company Size', 'remote_type': 'Type of Work'},
        barmode='relative', # Membantu menampakkan perbandingan peratusan
        color_discrete_sequence=px.colors.qualitative.Safe
    )
    st.plotly_chart(fig_bar_size, use_container_width=True)

    # Sunburst Chart untuk huraian hierarki yang interaktif
    st.markdown("---")
    st.write("#### 🎯 Company Size and Job Type Hierarchy")
    
    fig_sunburst = px.sunburst(
        df_size_remote,
        path=['company_size', 'remote_type'],
        values='count',
        title="Sunburst Chart: Job Distribution Based on Company Size",
        color='remote_type',
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig_sunburst, use_container_width=True)


# ==========================================
# TAB 2: INDUSTRY VS REMOTE TYPE
# ==========================================
with tab2:
    st.subheader("2. Work Policy Based on Type of Industry")
    st.markdown("Studying the adaptation of flexible working across various industry sectors.")

    # Tapis industri menggunakan multiselect (Interaktif!)
    all_industries = df['company_industry'].unique()
    selected_industries = st.multiselect(
        "Select an Industry to Compare:",
        options=all_industries,
        default=all_industries[:5] # Default letak 5 yang pertama supaya tidak semak
    )

    df_filtered_ind = df[df['company_industry'].isin(selected_industries)]
    df_ind_remote = df_filtered_ind.groupby(['company_industry', 'remote_type']).size().reset_index(name='count')

    # Grouped/Stacked Bar Chart untuk Industri
    fig_bar_ind = px.bar(
        df_ind_remote,
        x='company_industry',
        y='count',
        color='remote_type',
        title="Comparison of Work Policies by Industry",
        labels={'count': 'Number of Jobs', 'company_industry': 'Industry Type', 'remote_type': 'Type of Work'},
        barmode='group', # Bar diletakkan bersebelahan untuk senang banding
        color_discrete_sequence=px.colors.qualitative.Vivid
    )
    st.plotly_chart(fig_bar_ind, use_container_width=True)

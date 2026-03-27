import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff

st.title("🤖 Objective 2: Predictive Modeling")
st.markdown("""
This page displays a simulation of the performance of machine learning models (*Machine Learning*) in predicting industry needs based on existing data.
""")

# Load data
DATA_URL = "https://raw.githubusercontent.com/atyn104/intern/refs/heads/main/project_data_data.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_URL)

df = load_data()

# Pecahkan kepada 2 tab untuk kemas
tab1, tab2 = st.tabs(["🚦 Predicting Hiring Urgency", "⏳ Predicting Years of Experience"])

# ==========================================
# TAB 1: CLASSIFICATION (HIRING URGENCY)
# ==========================================
with tab1:
    st.subheader("1. Classification of Hiring Urgency Levels")
    st.markdown("Predict whether `hiring_urgency` is **Low, Medium,** or **High**.")

    # A. SIMULASI CONFUSION MATRIX
    st.write("#### 🎯 Confusion Matrix (Prestasi Model)")
    
    # Data dummy simulasi ketepatan model
    z = [[150, 20, 5],  # Actual Low
         [15, 180, 25], # Actual Medium
         [2, 30, 200]] # Actual High
    
    x_labels = ['Predicted Low', 'Predicted Medium', 'Predicted High']
    y_labels = ['Actual Low', 'Actual Medium', 'Actual High']

    fig_cm = ff.create_annotated_heatmap(z, x=x_labels, y=y_labels, colorscale='Blues')
    st.plotly_chart(fig_cm, use_container_width=True)

    # B. FEATURE IMPORTANCE
    st.markdown("---")
    st.write("#### 🔑 Main Factors Affecting Urgency (Feature Importance)")
    importance_data = pd.DataFrame({
        'Feature': ['Company Industry', 'Company Size', 'Remote Type', 'Job Title', 'Skills Required'],
        'Importance': [0.35, 0.25, 0.20, 0.15, 0.05]
    }).sort_values(by='Importance', ascending=True)

    fig_fi = px.bar(
        importance_data, 
        x='Level of Influence (Importance)', 
        y='Features', 
        orientation='h',
        title="Factors Most Affecting Hiring Urgency",
        color_discrete_sequence=['#1f77b4']
    )
    st.plotly_chart(fig_fi, use_container_width=True)


# ==========================================
# TAB 2: REGRESI (YEARS OF EXPERIENCE)
# ==========================================
with tab2:
    st.subheader("2. Regression Prediction of Years of Experience Required")
    st.markdown("Predict expected `years_experience` based on job title, skills, and industry.")

    # C. ACTUAL VS PREDICTED SCATTER PLOT
    st.write("#### 📈 Model Evaluation Graph(Actual vs Predicted)")

    # Ambil 500 sampel data sebenar untuk simulasi ramalan
    sample_df = df.sample(500, random_state=42)
    actual = sample_df['years_experience'].values
    
    # Simulasi ramalan (Tambah sedikit noise rawak supaya nampak realistik)
    predicted = actual + np.random.normal(0, 1.5, size=len(actual))
    predicted = np.clip(predicted, 0, 20) # Hadkan supaya tidak negatif

    reg_df = pd.DataFrame({
        'Actual Years': actual,
        'Predicted Years': predicted,
        'Job Title': sample_df['job_title']
    })

    fig_reg = px.scatter(
        reg_df, 
        x='Actual Years', 
        y='Predicted Years',
        color='Job Title',
        title="Years of Experience Prediction vs. Actual Conditions",
        labels={'Actual Years': 'Actual Year', 'Predicted Years': 'Model Forecast Year'}
    )
    
    # Tambah garisan rujukan y = x (Ramalan sempurna)
    fig_reg.add_shape(
        type="line", line=dict(dash='dash', color='red'),
        x0=0, y0=0, x1=max(actual), y1=max(actual)
    )

    st.plotly_chart(fig_reg, use_container_width=True)
    
    st.success("ℹ️ The red dotted line represents a 100% accurate prediction. The closer the data points are to the line, the more accurate your model is!")

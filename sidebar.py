import streamlit as st

st.set_page_config(
    page_title="💼 AI & Data Science Job Market Dashboard "
)

# 1. Definisi Halaman (Pastikan fail 'Performance Metrics.py', 'Objective 2.py', dan 'Objective 3.py' wujud)
home = st.Page('homepage.py', title='Homepage', default=True, icon=":material/home:")
objective1 = st.Page('obj number 1.py', title='Objective 1', icon=":material/ads_click:")
objective2 = st.Page('obj number 2.py', title='Objective 2', icon=":material/ads_click:")
objective3 = st.Page('obj number 3.py', title='Objective 3', icon=":material/ads_click:")

# 2. Tambahkan semua halaman ke dalam navigasi
# Semua halaman dalam senarai akan dipaparkan di bawah tajuk 'Menu'
pg = st.navigation(
        {
            "Menu": [home, visualise, objective2, objective3]
        }
    )

pg.run()

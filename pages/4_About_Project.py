import streamlit as st
from utils.styles import load_styles
from utils.toggle import mobile_toggle
from utils.sidebar import show_sidebar


st.set_page_config(
    page_title="About Project",
    page_icon="ℹ️",
    layout="wide"
)

load_styles()
mobile_toggle()
show_sidebar()

st.markdown("## ℹ️ About This Project")
st.markdown("---")

# Project Overview
st.markdown("""
<div style='background:white; padding:30px; border-radius:15px;
            box-shadow:0 2px 10px rgba(0,0,0,0.08);'>
    <h3 style='color:#2D1B69;'>🎯 Project Overview</h3>
    <p style='color:grey; font-size:15px; line-height:1.8;'>
        This AI-powered system predicts student academic performance using 
        Machine Learning and recommends suitable career paths based on 
        interests and academic profile.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")

# 3 Info Cards
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div style='background:white; padding:25px; border-radius:15px;
                box-shadow:0 2px 10px rgba(0,0,0,0.08);
                border-top:4px solid #4299E1;'>
        <h4 style='color:#2D1B69;'>🤖 ML Model Used</h4>
        <p style='color:grey; font-size:14px;'>Linear Regression trained on 2392 student records with 95.3% R² accuracy.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div style='background:white; padding:25px; border-radius:15px;
                box-shadow:0 2px 10px rgba(0,0,0,0.08);
                border-top:4px solid #48BB78;'>
        <h4 style='color:#2D1B69;'>📊 Dataset</h4>
        <p style='color:grey; font-size:14px;'>Students Performance Dataset from Kaggle with 15 features including study habits and activities.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div style='background:white; padding:25px; border-radius:15px;
                box-shadow:0 2px 10px rgba(0,0,0,0.08);
                border-top:4px solid #805AD5;'>
        <h4 style='color:#2D1B69;'>🛠️ Tech Stack</h4>
        <p style='color:grey; font-size:14px;'>Python, Streamlit, Scikit-learn, Pandas, Plotly for interactive visualizations.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.markdown("---")

# How it Works
st.markdown("### ⚙️ How It Works")

w1, w2, w3, w4 = st.columns(4)

with w1:
    st.markdown("""
    <div style='background:white; padding:20px; border-radius:15px;
                box-shadow:0 2px 10px rgba(0,0,0,0.08); text-align:center;'>
        <div style='font-size:35px;'>📝</div>
        <h4 style='color:#2D1B69;'>Step 1</h4>
        <p style='color:grey; font-size:13px;'>Fill Student Profile with academic details and interests</p>
    </div>
    """, unsafe_allow_html=True)

with w2:
    st.markdown("""
    <div style='background:white; padding:20px; border-radius:15px;
                box-shadow:0 2px 10px rgba(0,0,0,0.08); text-align:center;'>
        <div style='font-size:35px;'>🤖</div>
        <h4 style='color:#2D1B69;'>Step 2</h4>
        <p style='color:grey; font-size:13px;'>ML model predicts GPA based on study habits</p>
    </div>
    """, unsafe_allow_html=True)

with w3:
    st.markdown("""
    <div style='background:white; padding:20px; border-radius:15px;
                box-shadow:0 2px 10px rgba(0,0,0,0.08); text-align:center;'>
        <div style='font-size:35px;'>📊</div>
        <h4 style='color:#2D1B69;'>Step 3</h4>
        <p style='color:grey; font-size:13px;'>Performance score calculated from predicted GPA</p>
    </div>
    """, unsafe_allow_html=True)

with w4:
    st.markdown("""
    <div style='background:white; padding:20px; border-radius:15px;
                box-shadow:0 2px 10px rgba(0,0,0,0.08); text-align:center;'>
        <div style='font-size:35px;'>🎯</div>
        <h4 style='color:#2D1B69;'>Step 4</h4>
        <p style='color:grey; font-size:13px;'>Career paths recommended based on interests + performance</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.markdown("---")
st.markdown("""
<div style='background:#EBF8FF; padding:15px; border-radius:10px; color:#2B6CB0; font-size:13px;'>
    💡 This project demonstrates the use of Machine Learning in Education Technology (EdTech) 
    to provide personalized academic guidance and career counseling to students.
</div>
""", unsafe_allow_html=True)


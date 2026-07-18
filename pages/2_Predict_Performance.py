import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go # Imports Plotly Graph Objects. Purpose--> Create interactive charts. Here it is used for the GPA Gauge.
from utils.styles import load_styles
from utils.sidebar import show_sidebar

st.set_page_config(
    page_title="Predict Performance",
    page_icon="📊",
    layout="wide"
)

model = joblib.load('gpa_model.pkl')
model_columns = joblib.load('model_columns.pkl')

load_styles()
show_sidebar()

st.markdown("## 📊 Predict Performance")
st.markdown("Your predicted academic performance based on saved profile.")
st.markdown("---")

if 'study_time' not in st.session_state:
    st.warning("⚠️ Please fill your Student Profile first!")
    st.stop()
study_time = st.session_state['study_time']
absences = st.session_state['absences']
age = st.session_state['age']
gender = st.session_state['gender']
parental_education = st.session_state['parental_education']
parental_support = st.session_state['parental_support']
tutoring = st.session_state['tutoring']
extracurricular = st.session_state['extracurricular']
sports = st.session_state['sports']
music = st.session_state['music']
volunteering = st.session_state['volunteering']
name = st.session_state.get('name', 'Student')
student_data = {
    'Age': age,
    'Gender': gender,
    'Ethnicity': 0,
    'ParentalEducation': parental_education,
    'StudyTimeWeekly': study_time,
    'Absences': absences,
    'Tutoring': tutoring,
    'ParentalSupport': parental_support,
    'Extracurricular': extracurricular,
    'Sports': sports,
    'Music': music,
    'Volunteering': volunteering
}

input_df = pd.DataFrame([student_data])[model_columns]
predicted_gpa = model.predict(input_df)[0]
predicted_gpa = round(max(0, min(4, predicted_gpa)), 2)
st.session_state['predicted_gpa'] = predicted_gpa
predicted_percentage = round((predicted_gpa / 4) * 100, 1)
if predicted_gpa >= 3.5:
    grade = "A"
    grade_color = "#48BB78"
    grade_text = "Excellent Performance!"
    tier = "STRONG TRAJECTORY"
elif predicted_gpa >= 3.0:
    grade = "B"
    grade_color = "#4299E1"
    grade_text = "Good Performance!"
    tier = "GOOD PROGRESS"
elif predicted_gpa >= 2.0:
    grade = "C"
    grade_color = "#ECC94B"
    grade_text = "Average Performance"
    tier = "NEEDS IMPROVEMENT"
else:
    grade = "D"
    grade_color = "#FC8181"
    grade_text = "Below Average"
    tier = "NEEDS ATTENTION"
st.markdown(f"### 👋 Hello, {name}! Here are your predicted results.")

r1, r2, r3 = st.columns(3)

with r1:
    st.markdown(f"""
    <div style='background:white; padding:20px; border-radius:15px;
                box-shadow:0 2px 10px rgba(0,0,0,0.08); text-align:center;'>
        <p style='color:grey; font-size:13px; margin:0;'>Predicted GPA</p>
        <h1 style='color:#4299E1; margin:10px 0;'>{predicted_gpa}</h1>
        <p style='color:grey; font-size:12px; margin:0;'>out of 4.0</p>
    </div>
    """, unsafe_allow_html=True)

with r2:
    st.markdown(f"""
    <div style='background:white; padding:20px; border-radius:15px;
                box-shadow:0 2px 10px rgba(0,0,0,0.08); text-align:center;'>
        <p style='color:grey; font-size:13px; margin:0;'>Performance Score</p>
        <h1 style='color:{grade_color}; margin:10px 0;'>{predicted_percentage}%</h1>
        <p style='color:{grade_color}; font-size:12px; margin:0;'>{grade_text}</p>
    </div>
    """, unsafe_allow_html=True)

with r3:
    st.markdown(f"""
    <div style='background:white; padding:20px; border-radius:15px;
                box-shadow:0 2px 10px rgba(0,0,0,0.08); text-align:center;'>
        <p style='color:grey; font-size:13px; margin:0;'>Grade</p>
        <h1 style='color:{grade_color}; margin:10px 0;'>{grade}</h1>
        <p style='color:grey; font-size:12px; margin:0;'>{tier}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
g_col, info_col = st.columns([1, 1])

with g_col:
    st.markdown("#### 🎯 GPA Gauge")
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=predicted_gpa,
        number={'suffix': " / 4.0", 'font': {'size': 36, 'color': '#4299E1'}},
        gauge={
            'axis': {'range': [0, 4]},
            'bar': {'color': grade_color},
            'steps': [
                {'range': [0, 2], 'color': '#FED7D7'},
                {'range': [2, 3], 'color': '#FEFCBF'},
                {'range': [3, 4], 'color': '#C6F6D5'}
            ],
        },
        title={'text': "Predicted GPA", 'font': {'size': 14, 'color': 'grey'}}
    ))
    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=50, b=20),
        paper_bgcolor='white'
    )
    st.plotly_chart(fig, use_container_width=True)

with info_col:
    st.markdown("#### 📋 Performance Summary")
    st.markdown(f"""
    <div style='background:white; padding:25px; border-radius:15px;
                box-shadow:0 2px 10px rgba(0,0,0,0.08); margin-top:10px;'>
        <p><b>Student Name:</b> {name}</p>
        <p><b>Predicted GPA:</b> {predicted_gpa} / 4.0</p>
        <p><b>Performance:</b> {predicted_percentage}%</p>
        <p><b>Grade:</b> <span style='color:{grade_color}; font-weight:bold;'>{grade} — {grade_text}</span></p>
        <p><b>Weekly Study Time:</b> {study_time} hours</p>
        <p><b>Absences:</b> {absences}</p>
        <p><b>Trajectory:</b> <span style='color:{grade_color}; font-weight:bold;'>{tier}</span></p>
    </div>
    """, unsafe_allow_html=True)

    if predicted_gpa >= 3.5:
        st.balloons()
        st.success("🎉 Outstanding! Keep up the excellent work!")
    elif predicted_gpa >= 2.5:
        st.info("📚 Good progress! A little more effort can take you to the top.")
    else:
        st.warning("⚠️ Focus on reducing absences and increasing study time.")

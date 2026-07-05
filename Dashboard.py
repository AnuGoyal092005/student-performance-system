import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
from utils.styles import load_styles
from utils.toggle import mobile_toggle
from utils.sidebar import show_sidebar

st.set_page_config(
    page_title="Student Performance System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)
model=joblib.load("gpa_model.pkl")
model_columns=joblib.load("model_columns.pkl")

if 'study_time' in st.session_state:
    student_data = {
        'Age': st.session_state['age'],
        'Gender': st.session_state['gender'],
        'Ethnicity': 0,
        'ParentalEducation': st.session_state['parental_education'],
        'StudyTimeWeekly': st.session_state['study_time'],
        'Absences': st.session_state['absences'],
        'Tutoring': st.session_state['tutoring'],
        'ParentalSupport': st.session_state['parental_support'],
        'Extracurricular': st.session_state['extracurricular'],
        'Sports': st.session_state['sports'],
        'Music': st.session_state['music'],
        'Volunteering': st.session_state['volunteering']
    }
    input_df = pd.DataFrame([student_data])[model_columns]
    predicted_gpa = round(max(0, min(4, model.predict(input_df)[0])), 2)
    performance = round((predicted_gpa / 4) * 100, 1)
    improvement = round(100 - performance, 1)
    student_name = st.session_state.get('name', 'Student')
else:
    predicted_gpa = 0
    performance = 0
    improvement = 0
    student_name = "Student"

load_styles()
mobile_toggle()
show_sidebar()
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("## Dashboard")
    st.markdown(f"Welcome back, {student_name}! Here's an overview of your performance.")

with col2:
    st.markdown("""
    <div style='text-align:right; padding:10px;'>
        <img src='https://www.w3schools.com/howto/img_avatar.png' 
             width='45' style='border-radius:50%; vertical-align:middle;'>
        &nbsp;
        <span style='color:grey; font-size:12px; margin-right:5px;'>Student</span>
    </div>
    """, unsafe_allow_html=True)
    
st.markdown("---")
card1, card2=st.columns(2)

with card1:
     st.markdown(f"""
    <div style='background:white; padding:20px; border-radius:15px; 
                box-shadow:0 2px 10px rgba(0,0,0,0.08);'>
        <span style='font-size:35px;'>📘</span>
        <p style='color:grey; margin:8px 0 4px 0; font-size:13px;'>Overall Performance (Predicted)</p>
        <h2 style='color:#4299E1; margin:0;'>{performance}%</h2>
        <p style='color:#4299E1; margin:4px 0 0 0; font-size:13px;'>{'Good' if performance >= 70 else 'Keep Improving'}</p>
    </div>
    """, unsafe_allow_html=True)

with card2:
    st.markdown(f"""
    <div style='background:white; padding:20px; border-radius:15px;
                box-shadow:0 2px 10px rgba(0,0,0,0.08);'>
        <span style='font-size:35px;'>📈</span>
        <p style='color:grey; margin:8px 0 4px 0; font-size:13px;'>Improvement Potential</p>
        <h2 style='color:#48BB78; margin:0;'>{improvement}%</h2>
        <p style='color:#48BB78; margin:4px 0 0 0; font-size:13px;'>Keep it up!</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
perf_col, chart_col=st.columns([1, 1])

with perf_col:
    st.markdown("### Performance Prediction")
    fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=performance,
    number={'suffix': "%", 'font': {'size': 40, 'color': '#4299E1'}},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': '#4299E1'},
        'bgcolor': 'white',
        'steps': [
            {'range': [0, 40], 'color': '#FED7D7'},
            {'range': [40, 70], 'color': '#FEFCBF'},
            {'range': [70, 100], 'color': '#C6F6D5'}
        ],
    },
    title={'text': "Predicted Score", 'font': {'size': 14, 'color': 'grey'}}
))
    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=50, b=20),
        paper_bgcolor='white',
        font=dict(family='sans-serif')
    )
    st.plotly_chart(fig, use_container_width=True)
    st.info("Consistent study and practice can improve your score further.")

st.markdown("---")
st.markdown("### Career Recommendations for You")

if 'study_time' in st.session_state:
    music = st.session_state['music']
    volunteering = st.session_state['volunteering']
    interest_coding = st.session_state['interest_coding']
    interest_science = st.session_state['interest_science']
    interest_business = st.session_state['interest_business']
    interest_arts = st.session_state['interest_arts']
    interest_social = st.session_state['interest_social']

    gpa = st.session_state.get('predicted_gpa', 2.0)

    career_scores = {
    'Software Developer': (interest_coding * 0.5 + interest_science * 0.3 + gpa * 0.2),
    'Data Scientist': (interest_coding * 0.4 + interest_science * 0.4 + gpa * 0.2),
    'AI / ML Engineer': (interest_coding * 0.3 + interest_science * 0.5 + gpa * 0.2),
    'Business Analyst': (interest_business * 0.5 + interest_coding * 0.3 + gpa * 0.2),
    'Doctor / Healthcare': (interest_science * 0.6 + interest_social * 0.2 + gpa * 0.2),
    'Teacher / Educator': (interest_social * 0.5 + interest_science * 0.3 + gpa * 0.2),
    'Artist / Designer': (interest_arts * 0.7 + interest_social * 0.1 + gpa * 0.2),
    'Entrepreneur': (interest_business * 0.6 + interest_coding * 0.2 + gpa * 0.2),
}

    sorted_careers = sorted(career_scores.items(), key=lambda x: x[1], reverse=True)
    top_3 = sorted_careers[:3]

    career_emojis = {
        'Software Developer': '💻',
        'Data Scientist': '📊',
        'AI / ML Engineer': '🤖',
        'Business Analyst': '📈',
        'Doctor / Healthcare': '🩺',
        'Teacher / Educator': '📚',
        'Artist / Designer': '🎨',
        'Entrepreneur': '🚀'
    }
    career_colors = ['#4299E1', '#48BB78', '#805AD5']

    career1, career2, career3 = st.columns(3)
    cols = [career1, career2, career3]

    for i, (career, score) in enumerate(top_3):
        match_percent = round(score * 10, 1)
        emoji = career_emojis.get(career, '🎯')
        with cols[i]:
            st.markdown(f"""
            <div style='background:white; padding:20px; border-radius:15px;
                        box-shadow:0 2px 10px rgba(0,0,0,0.08);'>
                <span style='font-size:40px;'>{emoji}</span>
                <h4 style='margin:10px 0 5px 0; color:#1A202C;'>{career}</h4>
                <br>
                <p style='color:{career_colors[i]}; font-weight:bold; margin:0;'>Match: {match_percent}%</p>
            </div>
            """, unsafe_allow_html=True)
else:
    career1, career2, career3 = st.columns(3)
    with career1:
        st.markdown("""
        <div style='background:white; padding:20px; border-radius:15px;
                    box-shadow:0 2px 10px rgba(0,0,0,0.08);'>
            <span style='font-size:40px;'>💻</span>
            <h4 style='margin:10px 0 5px 0;'>Fill Profile First</h4>
            <p style='color:grey; font-size:13px;'>Save your profile to see personalized career recommendations.</p>
        </div>
        """, unsafe_allow_html=True)

        

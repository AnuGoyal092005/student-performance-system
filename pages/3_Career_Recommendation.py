import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Career Recommendation",
    page_icon="🎯",
    layout="wide"
)

st.markdown("""
<style>
[data-testid="stSidebarCollapseButton"] {
    display: none !important;
}
            
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #2D1B69 0%, #11047A 100%);
}
[data-testid="stSidebar"] * {
    color: white !important;
}
[data-testid="stSidebarNav"] {
    display: none !important;
}
[data-testid="stSidebarUserContent"] {
    position: absolute;
    top: 0;
    width: 100%;
    padding-top: 20px;
}
[data-testid="stSidebar"] .stButton > button {
    background: transparent !important;
    border: none !important;
    color: white !important;
    text-align: left !important;
    font-size: 15px !important;
    padding: 8px 15px !important;
    border-radius: 8px !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(255,255,255,0.15) !important;
}
#MainMenu, footer, header {
    visibility: hidden;
}
.stApp {
    background: #F4F7FE;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("# 🎓")
    st.markdown("### Student Performance Prediction & Career Recommendation System")
    st.markdown("---")
    if st.button("🏠 Dashboard", use_container_width=True):
        st.switch_page("Dashboard.py")
    if st.button("👤 Student Profile", use_container_width=True):
        st.switch_page("pages/1_Student_Profile.py")
    if st.button("📊 Predict Performance", use_container_width=True):
        st.switch_page("pages/2_Predict_Performance.py")
    if st.button("🎯 Career Recommendation", use_container_width=True):
        st.switch_page("pages/3_Career_Recommendation.py")
    if st.button("ℹ️ About Project", use_container_width=True):
        st.switch_page("pages/4_About_Project.py")

st.markdown("## 🎯 Career Recommendation")
st.markdown("Based on your academic performance and interests, here are your best career matches.")
st.markdown("---")
if 'study_time' not in st.session_state:
    st.warning("⚠️ Please fill your Student Profile first!")
    st.stop()

study_time = st.session_state['study_time']
music = st.session_state['music']
volunteering = st.session_state['volunteering']
interest_coding = st.session_state['interest_coding']
interest_science = st.session_state['interest_science']
interest_business = st.session_state['interest_business']
interest_arts = st.session_state['interest_arts']
interest_social = st.session_state['interest_social']
name = st.session_state.get('name', 'Student')

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
best_career = top_3[0][0]

career_info = {
    'Software Developer': {
        'emoji': '💻',
        'desc': 'Design, develop and maintain software applications.',
        'salary': '₹6L – ₹25L /yr',
        'skills': 'Python, Java, Problem Solving',
        'color': '#4299E1'
    },
    'Data Scientist': {
        'emoji': '📊',
        'desc': 'Analyze data and build models to solve real-world problems.',
        'salary': '₹8L – ₹30L /yr',
        'skills': 'Python, Statistics, Machine Learning',
        'color': '#48BB78'
    },
    'AI / ML Engineer': {
        'emoji': '🤖',
        'desc': 'Work on artificial intelligence and machine learning models.',
        'salary': '₹10L – ₹35L /yr',
        'skills': 'Deep Learning, Python, Mathematics',
        'color': '#805AD5'
    },
    'Business Analyst': {
        'emoji': '📈',
        'desc': 'Bridge the gap between business needs and technology solutions.',
        'salary': '₹5L – ₹20L /yr',
        'skills': 'Excel, SQL, Communication',
        'color': '#E2A33D'
    },
    'Doctor / Healthcare': {
        'emoji': '🩺',
        'desc': 'Diagnose and treat patients, improve public health.',
        'salary': '₹8L – ₹30L /yr',
        'skills': 'Biology, Chemistry, Empathy',
        'color': '#FC8181'
    },
    'Teacher / Educator': {
        'emoji': '📚',
        'desc': 'Shape future generations through quality education.',
        'salary': '₹3L – ₹12L /yr',
        'skills': 'Communication, Patience, Subject Knowledge',
        'color': '#F6AD55'
    },
    'Artist / Designer': {
        'emoji': '🎨',
        'desc': 'Create visual and creative work that communicates ideas.',
        'salary': '₹3L – ₹15L /yr',
        'skills': 'Creativity, Design Tools, Aesthetics',
        'color': '#ED64A6'
    },
    'Entrepreneur': {
        'emoji': '🚀',
        'desc': 'Build and grow your own business or startup.',
        'salary': '₹0 – Unlimited',
        'skills': 'Leadership, Risk Taking, Innovation',
        'color': '#667EEA'
    },
}

st.markdown(f"### 🌟 Top Career Matches for {name}")
st.markdown("Based on your interests and academic profile:")
st.write("")

col1, col2, col3 = st.columns(3)
cols = [col1, col2, col3]

for i, (career, score) in enumerate(top_3):
    info = career_info[career]
    match_percent = round(score * 10, 1)
    
    with cols[i]:
        st.markdown(f"""
        <div style='background:white; padding:25px; border-radius:15px;
                    box-shadow:0 2px 10px rgba(0,0,0,0.08);
                    border-top: 4px solid {info["color"]};'>
            <div style='font-size:45px; text-align:center;'>{info["emoji"]}</div>
            <h4 style='text-align:center; color:#1A202C; margin:10px 0 5px 0;'>{career}</h4>
            <p style='color:grey; font-size:13px; text-align:center;'>{info["desc"]}</p>
            <hr style='border:1px solid #F4F7FE;'>
            <p style='margin:5px 0;'><b>💰 Salary:</b> {info["salary"]}</p>
            <p style='margin:5px 0;'><b>🛠️ Skills:</b> {info["skills"]}</p>
            <br>
            <p style='color:{info["color"]}; font-weight:bold; font-size:18px; text-align:center;'>
                Match: {match_percent}%
            </p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("### 📊 All Career Match Scores")

all_careers = list(career_scores.keys())
all_scores = [round(min(s * 10, 99), 1) for s in career_scores.values()]
colors = [career_info[c]['color'] for c in all_careers]

bar_fig = go.Figure(go.Bar(
    x=all_careers,
    y=all_scores,
    marker_color=colors,
    text=all_scores,
    textposition='outside'
))

bar_fig.update_layout(
    height=400,
    margin=dict(l=20, r=20, t=30, b=100),
    paper_bgcolor='white',
    plot_bgcolor='white',
    yaxis=dict(range=[0, 110]),
    xaxis=dict(tickangle=-20),
    showlegend=False
)

st.plotly_chart(bar_fig, use_container_width=True)


st.markdown("---")
best_info = career_info[best_career]
st.markdown(f"""
<div style='background: linear-gradient(135deg, #2D1B69, #11047A);
            padding:30px; border-radius:15px; color:white; text-align:center;'>
    <h2>🏆 Your Best Career Match</h2>
    <div style='font-size:60px;'>{best_info["emoji"]}</div>
    <h2 style='color:#F6E3C2;'>{best_career}</h2>
    <p style='color:#DDD; font-size:16px;'>{best_info["desc"]}</p>
    <p style='color:#E2A33D; font-size:20px; font-weight:bold;'>
        💰 {best_info["salary"]}
    </p>
    <p style='color:#DDD;'>🛠️ Key Skills: {best_info["skills"]}</p>
</div>
""", unsafe_allow_html=True)
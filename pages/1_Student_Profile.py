import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Student Profile",
    page_icon="👤",
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
#MainMenu, footer, header {
    visibility: hidden;
}
.stApp {
    background: #F4F7FE;
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
[data-testid="stSidebarNav"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 👤 Student Profile")
    st.markdown("Fill in your details below. This information will be used for performance prediction.")
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

col1, col2 = st.columns(2)
with col1:
    st.markdown("#### 📋 Personal Information")
    name = st.text_input("Full Name", placeholder="Enter your name")
    age = st.number_input("Age", min_value=14, max_value=35, value=14, step=1)
    gender = st.radio("Gender", options=["Male", "Female"], horizontal=True)
    parental_education = st.selectbox("Parental Education Level", 
        options=[0, 1, 2, 3, 4],
        format_func=lambda x: {
            0: "No Education",
            1: "High School",
            2: "Some College", 
            3: "Bachelor's Degree",
            4: "Higher Degree"
        }[x])
with col2:
    st.markdown("#### 📚 Academic Details")
    study_time = st.number_input("Weekly Study Time (hours)", min_value=0, max_value=25, value=10, step=1)
    absences = st.number_input("Number of Absences", min_value=0, max_value=30, value=5, step=1)
    parental_support = st.selectbox("Parental Support Level",
        options=[0, 1, 2, 3, 4],
        format_func=lambda x: {
            0: "None",
            1: "Low",
            2: "Moderate",
            3: "High",
            4: "Very High"
        }[x])
    tutoring = st.radio("Receiving Tutoring?", options=["Yes", "No"], horizontal=True)
st.markdown("---")
st.markdown("#### 🎯 Activities & Interests")

act1, act2, act3 = st.columns(3)

with act1:
    extracurricular = st.radio("Extracurricular Activities?", options=["Yes", "No"], horizontal=True)
    sports = st.radio("Sports Participation?", options=["Yes", "No"], horizontal=True)

with act2:
    music = st.radio("Music?", options=["Yes", "No"], horizontal=True)
    volunteering = st.radio("Volunteering?", options=["Yes", "No"], horizontal=True)

with act3:
    interest_coding = st.number_input("Interest in Coding (0-10)", min_value=0, max_value=10, value=5)
    interest_science = st.number_input("Interest in Science (0-10)", min_value=0, max_value=10, value=5)
int1, int2, int3 = st.columns(3)

with int1:
    interest_business = st.number_input("Interest in Business (0-10)", min_value=0, max_value=10, value=5)

with int2:
    interest_arts = st.number_input("Interest in Arts (0-10)", min_value=0, max_value=10, value=5)

with int3:
    interest_social = st.number_input("Interest in Social Work (0-10)", min_value=0, max_value=10, value=5)
st.markdown("---")
save_col1, save_col2, save_col3 = st.columns([1, 1, 1])

with save_col2:
    if st.button("💾 Save Profile", use_container_width=True):
        st.session_state['name'] = name
        st.session_state['age'] = age
        st.session_state['gender'] = 1 if gender == "Female" else 0
        st.session_state['parental_education'] = parental_education
        st.session_state['study_time'] = study_time
        st.session_state['absences'] = absences
        st.session_state['parental_support'] = parental_support
        st.session_state['tutoring'] = 1 if tutoring == "Yes" else 0
        st.session_state['extracurricular'] = 1 if extracurricular == "Yes" else 0
        st.session_state['sports'] = 1 if sports == "Yes" else 0
        st.session_state['music'] = 1 if music == "Yes" else 0
        st.session_state['volunteering'] = 1 if volunteering == "Yes" else 0
        st.session_state['interest_coding'] = interest_coding
        st.session_state['interest_science'] = interest_science
        st.session_state['interest_business'] = interest_business
        st.session_state['interest_arts'] = interest_arts
        st.session_state['interest_social'] = interest_social
        st.success("✅ Profile saved! Go to Predict Performance page.")
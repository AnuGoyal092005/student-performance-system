import streamlit as st

def show_sidebar():

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
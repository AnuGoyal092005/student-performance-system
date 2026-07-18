import streamlit as st

def show_sidebar():
    with st.sidebar: # with tells Python that everything inside this block should appear inside the sidebar.  It refers to the sidebar section of the Streamlit app.
        st.markdown("# 🎓")
        st.markdown("### Student Performance Prediction & Career Recommendation System")
        st.markdown("---") # It separates the title from the navigation buttons.
        if st.button("🏠 Dashboard", use_container_width=True): # This line creates a full-width Dashboard button and checks if the user clicks it.
            st.switch_page("Dashboard.py") # This line navigates the user to the Dashboard page.
        if st.button("👤 Student Profile", use_container_width=True):
            st.switch_page("pages/1_Student_Profile.py")
        if st.button("📊 Predict Performance", use_container_width=True):
            st.switch_page("pages/2_Predict_Performance.py")
        if st.button("🎯 Career Recommendation", use_container_width=True):
            st.switch_page("pages/3_Career_Recommendation.py")
        if st.button("ℹ️ About Project", use_container_width=True):
            st.switch_page("pages/4_About_Project.py")

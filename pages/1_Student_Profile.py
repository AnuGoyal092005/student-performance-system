import streamlit as st  # Imports the Streamlit library., as st creates a short name (st) so we don't have to write streamlit every time.
import pandas as pd # Imports the Pandas library., pd is the short name., Although this file does not use Pandas directly, it is commonly imported for handling datasets.
from utils.styles import load_styles # Imports the function load_styles() from the styles.py file inside the utils folder.
from utils.sidebar import show_sidebar # Imports the function show_sidebar().

st.set_page_config( # Sets the basic configuration of the webpage.
    page_title="Student Profile", # Sets the browser tab title.
    page_icon="👤", # Adds an icon to the browser tab.
    layout="wide" # Makes the webpage use the full width of the screen.
)

load_styles() # Calls the CSS function.
show_sidebar() # Displays the sidebar.
col1, col2 = st.columns(2)
with col1: # Everything inside this block appears in the left column.
    st.markdown("#### 📋 Personal Information")
    name = st.text_input("Full Name", placeholder="Enter your name") # Creates a text box., Label of the text box., Shows a hint before typing.
    age = st.number_input("Age", min_value=14, max_value=35, value=14, step=1) # Creates a number input box.
    gender = st.radio("Gender", options=["Male", "Female"], horizontal=True)
    parental_education = st.selectbox("Parental Education Level", # Creates a dropdown.
        options=[0, 1, 2, 3, 4],
        format_func=lambda x: { # Lambda Function --> A lambda function is a short, anonymous function., Here it converts numbers into readable text.
            0: "No Education",
            1: "High School",
            2: "Some College", 
            3: "Bachelor's Degree",
            4: "Higher Degree"
        }[x])
with col2: # Everything appears in the right column.
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

act1, act2, act3 = st.columns(3) # Creates three equal columns.

with act1:
    extracurricular = st.radio("Extracurricular Activities?", options=["Yes", "No"], horizontal=True)
    sports = st.radio("Sports Participation?", options=["Yes", "No"], horizontal=True)

with act2:
    music = st.radio("Music?", options=["Yes", "No"], horizontal=True)
    volunteering = st.radio("Volunteering?", options=["Yes", "No"], horizontal=True)

with act3:
    interest_coding = st.number_input("Interest in Coding (0-10)", min_value=0, max_value=10, value=5)
    interest_science = st.number_input("Interest in Science (0-10)", min_value=0, max_value=10, value=5)
int1, int2, int3 = st.columns(3) # Creates another row with three columns.

with int1:
    interest_business = st.number_input("Interest in Business (0-10)", min_value=0, max_value=10, value=5)

with int2:
    interest_arts = st.number_input("Interest in Arts (0-10)", min_value=0, max_value=10, value=5)

with int3:
    interest_social = st.number_input("Interest in Social Work (0-10)", min_value=0, max_value=10, value=5)
st.markdown("---")
save_col1, save_col2, save_col3 = st.columns([1, 1, 1]) # Center the Save button by placing it in the middle column.

with save_col2: # Everything inside appears in the center column.
    if st.button("💾 Save Profile", use_container_width=True):
        st.session_state['name'] = name # Stores the entered name in Streamlit's session state., session_state keeps data available while the user navigates between pages.
        st.session_state['age'] = age
        st.session_state['gender'] = 1 if gender == "Female" else 0 # Uses a conditional expression (ternary operator)., This converts the text value into a numeric value for the machine learning model.
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
        st.success("✅ Profile saved! Go to Predict Performance page.") # Displays a green success message after the profile is saved.

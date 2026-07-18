import streamlit as st

def load_styles(): # This function contains all the custom CSS used to style the Streamlit application.
    st.markdown(""" # Here, we are  passing a multi-line string using triple quotes (""" ... """), which contains HTML and CSS.
    <style>
    /* Desktop pe >> button hide karo */
@media (min-width: 768px) {
    [data-testid="stSidebarCollapseButton"] {
        display: none !important;
    }
}
/* Sidebar Background */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #2D1B69 0%, #11047A 100%);
    }
    
    [data-testid="stSidebar"] * { color: white !important; }
    [data-testid="stSidebarNav"] { display: none !important; }
    [data-testid="stSidebarUserContent"] {
        position: absolute; top: 0; width: 100%; padding-top: 20px;
    }
/* Style Sidebar Buttons */
    
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
   #MainMenu,
footer {
    visibility: hidden;
}
    .stApp { background: #F4F7FE; }
    </style>
    """, unsafe_allow_html=True)

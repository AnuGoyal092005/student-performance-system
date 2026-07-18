import streamlit as st

def load_styles(): # This function contains all the custom CSS used to style the Streamlit application.
    st.markdown(""" # Here, we are  passing a multi-line string using triple quotes (""" ... """), which contains HTML and CSS.
    <style> # This starts a CSS block.
@media (min-width: 768px) { # Media Query--> Apply the following CSS only if the screen width is 768 pixels or more.
    [data-testid="stSidebarCollapseButton"] { # This selects Streamlit's sidebar collapse button (>>). data-testid is an HTML attribute used to identify elements.
        display: none !important; # display: none--> Completely hide the element. !important--> Force this rule even if another style exists.
    }
}
/* Sidebar Background */
    [data-testid="stSidebar"] { # Targets the entire sidebar.
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

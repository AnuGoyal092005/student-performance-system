import streamlit as st

def mobile_toggle():

    # Initialize state
    if "sidebar_open" not in st.session_state:
        st.session_state.sidebar_open = True

    # Mobile toggle button
    col1, col2 = st.columns([1, 12])

    with col1:
        if st.button("☰", key="mobile_toggle"):
            st.session_state.sidebar_open = not st.session_state.sidebar_open

    return st.session_state.sidebar_open

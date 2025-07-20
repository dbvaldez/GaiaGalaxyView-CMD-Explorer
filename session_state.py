import streamlit as st

def reset_flags():
    for flag in ["empty_result", "retry_search"]:
        if flag in st.session_state:
            st.session_state[flag] = False

def mark_empty():
    st.session_state.empty_result = True

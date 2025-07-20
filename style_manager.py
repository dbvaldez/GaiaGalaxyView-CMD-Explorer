# style_manager.py
import streamlit as st

def inject_custom_css():
    st.markdown("""
        <style>
            .stButton button {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
                border-radius: 6px;
            }
            .stWarning {
                font-size: 1rem;
            }
        </style>
    """, unsafe_allow_html=True)


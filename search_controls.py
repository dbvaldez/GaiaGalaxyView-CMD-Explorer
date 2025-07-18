import streamlit as st

def get_search_parameters():
    st.header("🔎 Star Search Controls")
    ra = st.number_input("RA (Right Ascension)", 0.0, 360.0, value=180.0)
    dec = st.number_input("Dec (Declination)", -90.0, 90.0, value=0.0)
    radius = st.slider("Search Radius (°)", 0.1, 5.0, value=0.5)
    auto_expand = st.checkbox("Auto-expand radius if no stars found", value=True)
    pm_threshold = st.slider("Minimum Proper Motion (mas/yr)", 0.0, 20.0, value=5.0)
    return ra, dec, radius, auto_expand, pm_threshold

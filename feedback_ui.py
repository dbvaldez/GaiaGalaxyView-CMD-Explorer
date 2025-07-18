import streamlit as st

def show_empty_result_ui():
    st.warning("No stars found in this region.")
    st.markdown("""
    **Suggestions:**
    - Increase search radius  
    - Relax filters like proper motion or magnitude  
    - Jump to sample regions:
        - Orion (RA 83.8°, Dec -5.4°)
        - Pleiades (RA 56.8°, Dec 24.1°)
    """)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Jump to Orion"):
            st.session_state["ra"] = 83.8
            st.session_state["dec"] = -5.4
            st.experimental_rerun()
    with col2:
        if st.button("Jump to Pleiades"):
            st.session_state["ra"] = 56.8
            st.session_state["dec"] = 24.1
            st.experimental_rerun()

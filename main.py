import streamlit as st
from feedback_ui import check_for_empty_results, show_empty_result_ui

def query_data(params):
    """Replace with your actual query logic."""
    # Simulate a failed query
    return []  # or None

def display_results(data):
    st.success("✅ Results loaded!")
    st.dataframe(data)  # Customize as needed

# --- App Start ---
st.title("GaiaGalaxyView CMD Explorer")

# Query inputs (replace with real inputs)
params = {"ra": 123.45, "dec": 67.89, "radius": 1.5}
results = query_data(params)

# Check if query returned results
check_for_empty_results(results)

# Show appropriate UI
if st.session_state.get("empty_result"):
    show_empty_result_ui()
else:
    display_results(results)

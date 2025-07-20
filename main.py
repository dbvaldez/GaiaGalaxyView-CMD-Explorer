import streamlit as st
from feedback_ui import check_for_empty_results, show_empty_result_ui
from query_utils import query_gaia_data
from gaia_parser import parse_gaia_response
from cmd_plotter import plot_cmd
from style_manager import inject_custom_css

# --- App Setup ---
st.set_page_config(page_title="GaiaGalaxyView CMD Explorer", layout="wide")
inject_custom_css()
st.title("✨ GaiaGalaxyView CMD Explorer")

# --- UI Inputs ---
ra = st.number_input("RA (deg)", value=123.45)
dec = st.number_input("DEC (deg)", value=67.89)
radius = st.slider("Search Radius (deg)", min_value=0.1, max_value=5.0, value=1.0)

# --- Query Execution ---
raw_data = query_gaia_data(ra, dec, radius)
parsed_data = parse_gaia_response(raw_data)

# --- Result Validation ---
check_for_empty_results(parsed_data)

# --- UI Routing ---
if st.session_state.get("empty_result"):
    show_empty_result_ui()
else:
    plot_cmd(parsed_data)

# --- Rerun-Flag Clearance (optional post-processing) ---
if st.session_state.get("retry_search"):
    st.session_state.retry_search = False

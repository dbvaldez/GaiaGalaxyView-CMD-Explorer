import streamlit as st
from search_controls import get_search_parameters
from gaia_query import fetch_star_data
from feedback_ui import show_empty_result_ui
from cmd_explorer import run_cmd_explorer

# -- App UI + Logic --
ra, dec, radius, auto_expand, pm_threshold = get_search_parameters()
stars, final_radius = fetch_star_data(ra, dec, radius, auto_expand)

if stars.empty:
    show_empty_result_ui()
else:
    st.success(f"{len(stars)} stars found within {final_radius:.1f}°")
    st.dataframe(stars)  # Swap with 3D visualization or vector plots

    with st.expander("📊 View CMD Explorer"):
        run_cmd_explorer(stars, final_radius, pm_threshold)

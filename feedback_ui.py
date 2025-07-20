import streamlit as st

def show_empty_result_ui():
    st.warning("🔍 No results found. Try adjusting your query or filters.")

    # Offer retry via a button, not auto-rerun
    if st.button("🔄 Retry Search"):
        st.session_state.retry_search = True  # Mark session flag
        st.experimental_rerun()


def check_for_empty_results(data):
    """Modular helper to decide if UI fallback is needed."""
    if data is None or len(data) == 0:
        st.session_state.empty_result = True
    else:
        st.session_state.empty_result = False

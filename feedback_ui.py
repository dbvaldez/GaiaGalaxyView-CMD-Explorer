import streamlit as st

def check_for_empty_results(data):
    """Marks session state if no data was found."""
    if data is None or len(data) == 0:
        st.session_state.empty_result = True
    else:
        st.session_state.empty_result = False

def show_empty_result_ui():
    """Displays a rerun-safe UI for when queries return no results."""
    st.warning("🚫 No results found. Try adjusting your query or filters!")

    # Optional suggestions
    st.markdown("#### 🛠 Tips for better results:")
    st.markdown("- Increase your search radius")
    st.markdown("- Loosen filters or constraints")
    st.markdown("- Try a broader query")

    # Retry button triggers rerun safely
    if st.button("🔄 Retry Search"):
        st.session_state.retry_search = True
        st.experimental_rerun()


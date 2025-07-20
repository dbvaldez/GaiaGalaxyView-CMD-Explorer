import streamlit as st

def check_for_empty_results(data):
    st.session_state.empty_result = data is None or len(data) == 0

def show_empty_result_ui():
    st.warning("🚫 No results found. Adjust your query and try again.")

    st.markdown("#### 🛠 Suggestions:")
    st.markdown("- Increase search radius")
    st.markdown("- Loosen filters or constraints")
    st.markdown("- Broaden your query area")

    if st.button("🔄 Retry Search"):
        st.session_state.retry_search = True
        st.experimental_rerun()


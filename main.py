from feedback_ui import show_empty_result_ui, check_for_empty_results

# After you run the query and get results
check_for_empty_results(results)

if st.session_state.get("empty_result"):
    show_empty_result_ui()
else:
    display_results(results)


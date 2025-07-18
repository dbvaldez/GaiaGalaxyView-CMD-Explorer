import streamlit as st
import plotly.express as px
import numpy as np

def run_cmd_explorer(stars_df, radius, pm_threshold):
    if stars_df.empty:
        st.info("No stars available for CMD plotting.")
        return

    stars_df["total_pm"] = (stars_df["pmra"]**2 + stars_df["pmdec"]**2)**0.5
    filtered = stars_df[stars_df["total_pm"] >= pm_threshold]

    if filtered.empty:
        st.warning("No stars meet the proper motion threshold.")
        return

    filtered["abs_mag"] = filtered["phot_g_mean_mag"] - 5 * (np.log10(1000 / filtered["parallax"]) - 1)

    fig = px.scatter(
        filtered, x="bp_rp", y="abs_mag",
        color="total_pm", color_continuous_scale="viridis",
        title=f"CMD within {radius:.1f}° — Proper Motion ≥ {pm_threshold} mas/yr",
        labels={"bp_rp": "BP–RP", "abs_mag": "Absolute G Magnitude"}
    )
    fig.update_yaxes(autorange="reversed")
    st.plotly_chart(fig, use_container_width=True)

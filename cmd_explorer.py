import plotly.express as px
import streamlit as st

def plot_cmd(dataframe):
    fig = px.scatter(
        dataframe,
        x="bp_rp",
        y="phot_g_mean_mag",
        hover_data=["source_id", "ra", "dec"],
        labels={"bp_rp": "BP - RP", "phot_g_mean_mag": "G Magnitude"},
        title="Color-Magnitude Diagram"
    )
    fig.update_yaxes(autorange="reversed")
    st.plotly_chart(fig, use_container_width=True)

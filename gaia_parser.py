import pandas as pd
from io import StringIO

def parse_gaia_response(content):
    if not content:
        return None

    try:
        df = pd.read_csv(StringIO(content.decode("utf-8")))
        df = df.dropna(subset=["phot_g_mean_mag", "phot_bp_mean_mag", "phot_rp_mean_mag"])
        df["bp_rp"] = df["phot_bp_mean_mag"] - df["phot_rp_mean_mag"]
        return df
    except Exception as e:
        print("Parsing error:", e)
        return None

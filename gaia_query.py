import pandas as pd

def query_gaia(ra, dec, radius):
    # Replace this with actual Gaia query logic
    return pd.DataFrame()  # Stub: returns empty for testing

def fetch_star_data(ra, dec, radius, auto_expand=True, retries=3, buffer_step=0.3):
    if not auto_expand:
        return query_gaia(ra, dec, radius), radius
    for _ in range(retries):
        stars = query_gaia(ra, dec, radius)
        if not stars.empty:
            return stars, radius
        radius += buffer_step
    return pd.DataFrame(), radius

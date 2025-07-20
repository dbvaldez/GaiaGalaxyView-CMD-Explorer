import requests

def query_gaia_data(ra, dec, radius):
    base_url = "https://gea.esac.esa.int/tap-server/tap"
    query = f"""
        SELECT TOP 5000 *
        FROM gaiadr3.gaia_source
        WHERE CONTAINS(
            POINT('ICRS', gaia_source.ra, gaia_source.dec),
            CIRCLE('ICRS', {ra}, {dec}, {radius})
        ) = 1
    """
    payload = {
        "request": "doQuery",
        "lang": "ADQL",
        "format": "csv",
        "query": query
    }

    try:
        response = requests.get(base_url, params=payload)
        response.raise_for_status()
        return response.content
    except Exception as e:
        print("Query failed:", e)
        return None

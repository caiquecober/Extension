import aiohttp
import pandas as pd

async def get_ts(series, api_key=None):
    if not api_key:
        raise ValueError("API key is required")

    url = f'https://api.eia.gov/v2/seriesid/{series}?api_key={api_key}'
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                raise Exception(f"Error fetching data: {response.status}")
            json_response = await response.json()

    # Process the JSON response
    nome = json_response.get('response').get('data')[0].get('series-description')
    df = pd.DataFrame(json_response.get('response').get('data'), columns=['period', 'value'])

    df_ts = df[['period', 'value']].copy()
    df_ts = df_ts.set_index('period')
    df_ts.columns = [nome]
    return df_ts
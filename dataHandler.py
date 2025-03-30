import requests
import pandas as pd
import os
from datetime import datetime

CRYPTO_API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 250,
    "page": 1
}

def fetch_crypto_data():
    response = requests.get(CRYPTO_API_URL, params=PARAMS)
    if response.status_code == 200:
        print("✅ Connection Successful! Fetching data...")
        data = response.json()
        df = pd.DataFrame(data)
        df = df[['id', 'current_price', 'market_cap', 'price_change_percentage_24h', 'ath', 'atl']]

        timestamp = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
        filename = f'crypto_data_{timestamp}.csv'

        df["time_stamp"] = timestamp
        df.to_csv(filename, index=False)
        print(f"✅ Data saved as {filename}")

        return filename
    else:
        print(f"❌ Failed to fetch data. Error code: {response.status_code}")
        return None

def load_latest_data():
    files = [f for f in os.listdir() if f.startswith("crypto_data_") and f.endswith(".csv")]
    latest_file = max(files, key=os.path.getctime) if files else None
    if not latest_file:
        raise FileNotFoundError("❌ No CSV file found. Please check the data fetching process.")

    df = pd.read_csv(latest_file)
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    numeric_columns = ["market_cap", "current_price", "price_change_percentage_24h", "ath", "atl"]
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df["time_stamp"] = pd.to_datetime(df["time_stamp"], format="%d-%m-%Y_%H-%M-%S", errors="coerce")

    return df

def get_top_cryptos(df, trend="gainers"):
    if trend == "gainers":
        df_sorted = df.sort_values(by="price_change_percentage_24h", ascending=False).head(10)
        title_suffix = "Top 10 Gainers"
    elif trend == "losers":
        df_sorted = df.sort_values(by="price_change_percentage_24h", ascending=True).head(10)
        title_suffix = "Top 10 Losers"
    else:
        raise ValueError("Invalid trend. Use 'gainers' or 'losers'.")
    
    return df_sorted, title_suffix

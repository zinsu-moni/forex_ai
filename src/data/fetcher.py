import requests

def get_latest_data(base, target):
    api_key = "d64f4a5b93334edd86378a12c9a2e999"  # Replace with your Twelve Data API key
    symbol = f"{base}/{target}"  # e.g., XAU/USD or EUR/USD
    url = f"https://api.twelvedata.com/price?symbol={symbol}&apikey={api_key}"

    response = requests.get(url)
    data = response.json()

    if "price" not in data:
        raise Exception("Failed to fetch rates: " + str(data))

    # Simulate an 'open' and 'close' price for AI decision (you can adjust logic)
    close = float(data["price"])
    open_price = close - 0.001  # Small difference for AI prediction logic
    return {'open': open_price, 'close': close}


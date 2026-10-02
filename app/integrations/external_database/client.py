import requests


class FMPClient:
    BASE_URL = "https://financialmodelingprep.com/stable"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_quote(self, symbol: str):
        url = f"{self.BASE_URL}/quote"

        params = {
            "symbol": symbol,
            "apikey": self.api_key
        }

        response = requests.get(url, params=params)

        response.raise_for_status()

        return response.json()

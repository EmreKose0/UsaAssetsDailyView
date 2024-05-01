import requests
import StoreProcedures as sp


def fetch_and_insert_assets():
    BASE_URL = "https://www.alphavantage.co/"
    API_KEY = open('C:\\Users\\emrek\\OneDrive\\Masaüstü\\pythonProject\\api_key', 'r').read()
    url_assets_list = BASE_URL + "query?function=TOP_GAINERS_LOSERS&apikey=demo"

    response = requests.get(url_assets_list).json()

    assets_dict = {}

    list_names = ['top_gainers', 'most_actively_traded', 'top_losers']
    for list_name in list_names:
        for item in response[list_name]:
            ticker = item['ticker']
            volume = item['volume']
            assets_dict[ticker] = volume

    print(assets_dict)

    for item in assets_dict.items():
        ticker = item[0]
        volume = item[1]
        sp.call_insert_assets_list(ticker, volume)


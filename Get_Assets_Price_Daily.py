import requests
import StoreProcedures as sp


def fetch_and_insert_assets_prices():
    try:
        BASE_URL = "https://www.alphavantage.co/"
        API_KEY = open('C:\\Users\\emrek\\OneDrive\\Masaüstü\\pythonProject\\api_key', 'r').read()

        ASSETS_CODE = sp.fetch_data_from_table()

        for code in ASSETS_CODE:
            url_assets_price = BASE_URL + "query?function=TIME_SERIES_DAILY&symbol=" + ASSETS_CODE[
                code] + "&apikey=" + API_KEY
            response = requests.get(url_assets_price).json()
            data = response["Time Series (Daily)"]
            for item in data:
                date = data[item]
                open_price = date['1. open']
                high_price = date['2. high']
                low_price = date['3. low']
                close_price = date['4. close']
                volume = date['5. volume']
                sp.call_insert_assets_price_daily(code, date, open_price, high_price, low_price, close_price, volume)

        print("Data successfully fetched and inserted into the database.")

    except Exception as e:
        print("Error:", e)


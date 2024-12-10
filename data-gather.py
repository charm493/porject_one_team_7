from os import environ
from requests import get

from pandas import DataFrame

def get_stock_data(symbol):
    """
    """

    alpha_vantage_api_key = environ["ALPHA_VANTAGE_API_KEY"]
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={symbol}&apikey={alpha_vantage_api_key}'

    resp = get(url)
    data = resp.json()["Weekly Adjusted Time Series"]

    df = DataFrame.from_dict(data, orient="index")

    return df


#  test
def get_all_stock_data():
    stock_data_map = {
        "Technology": {
            "ticker": "XLK",
            "name": "Technology Select Sector SPDR Fund"
        },
        "Healthcare": {
            "ticker": "XLV",
            "name": "Health Care Select Sector SPDR Fund"
        },
        "Financials": {
            "ticker": "XLF",
            "name": "Financial Select Sector SPDR Fund"
        },
        "Energy": {
            "ticker": "XLE",
            "name": "Energy Select Sector SPDR Fund"
        },
        "Consumer Goods": {
            "ticker": "XLP",
            "name": "Consumer Staples Select Sector SPDR Fund"
        },
        "Utilities": {
            "ticker": "XLU",
            "name": "Utilities Select Sector SPDR Fund"
        }
    }

    for sector, body in stock_data_map.items():
        ticker = body["ticker"]
        name = body["name"]

        raw_df = get_stock_data(ticker)
        raw_df.to_csv(f"{name}.csv")

get_all_stock_data()
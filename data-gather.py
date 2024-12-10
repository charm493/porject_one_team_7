from os import environ
from requests import get

from pandas import DataFrame

def get_stock_data(symbol):
    """Get stock data from Alpha Vantage, based on symbol (ticker).

    Args:
        symbol (str): ticker
    Returns:
        (pandas.DataFrame) stock data, with date indices
    """

    alpha_vantage_api_key = environ["ALPHA_VANTAGE_API_KEY"]
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={symbol}&apikey={alpha_vantage_api_key}'

    resp = get(url)
    data = resp.json()["Weekly Adjusted Time Series"]

    df = DataFrame.from_dict(data, orient="index")

    return df


STOCK_DATA_MAP = {
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

def bulk_get_stock_data(individual_sector=None):
    """Get stock data in bulk.

    Args:
        individual_sector (str): sector name
    Returns:
        (None)
    """


    for sector, body in STOCK_DATA_MAP.items():
        if (individual_sector is not None) and (individual_sector is not sector):
            pass
            
        ticker = body["ticker"]
        name = body["name"]

        raw_df = get_stock_data(ticker)
        raw_df.to_csv(f"raw_data/{name}.csv")

        print(f"Got stock data for sector ({sector}) and ticker ({ticker})")

bulk_get_stock_data()
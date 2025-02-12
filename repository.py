import pandas as pd


def get_data():
    portfolio = pd.read_csv(
        r"input\crisis_portfolio.csv",
        delimiter=",",
        index_col="Date",
        parse_dates=["Date"],
    )
    return portfolio


def get_begin_date():
    begin_date = "2008-01-01"
    return begin_date


def get_end_date():
    end_date = "2009-12-31"
    return end_date

def get_asset_price(portfolio,begin_date,end_date):
    asset_prices = portfolio.loc[begin_date:end_date]
    return asset_prices

def get_weights():
    weights = [0.25, 0.25, 0.25, 0.25]
    return weights

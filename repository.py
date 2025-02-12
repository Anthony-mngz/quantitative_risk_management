import pandas as pd


def getdata():
    portfolio = pd.read_csv(
        r"input\crisis_portfolio.csv",
        delimiter=",",
        index_col="Date",
        parse_dates=["Date"],
    )
    return portfolio


def getdate():
    begin_date =
    end_date =


def getassetprice(portfolio):
    asset_prices = portfolio.loc["2008-01-01":"2009-12-31"]
    return asset_prices

def get_weights():
    weights = [0.25, 0.25, 0.25, 0.25]
    return weights

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from repository import get_data, get_begin_date, get_end_date, get_asset_price, get_weights
from view import asset_price_plot, portfolio_returns_plot, display_covariance, display_pf_volatility, \
    display_volatility_serie
from model import compute_pf_daily_return, portfolio_return, covariance, annualized_covariance, portfolio_volatility, \
    portfolio_variance, thirty_days_rolling, annualized_volatility


def main():
    data = get_data()
    begin_date = get_begin_date()
    end_date = get_end_date()

    asset_price = get_asset_price(data, begin_date, end_date)
    asset_price_plot(asset_price)

    weights = get_weights()
    asset_returns = compute_pf_daily_return(asset_price)
    pf_returns = portfolio_return(asset_returns, weights)
    portfolio_returns_plot(pf_returns)

    cov = covariance(asset_returns)
    annualized_covariance(cov)
    display_covariance(cov)

    pf_variance = portfolio_variance(cov, weights)
    pf_volatility = portfolio_volatility(pf_variance)
    display_pf_volatility(pf_volatility)

    returns_windowed = thirty_days_rolling(pf_returns)
    volatility_serie = annualized_volatility(returns_windowed)
    display_volatility_serie(volatility_serie)


if __name__ == "__main__":
    main()

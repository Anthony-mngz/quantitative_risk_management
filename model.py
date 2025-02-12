import numpy as np


# Compute the portfolio's daily returns
def compute_pf_daily_return(asset_prices):
    asset_returns = asset_prices.pct_change()
    return asset_returns


def portfolio_return(asset_returns, weights):
    portfolio_returns = asset_returns.dot(weights)
    return portfolio_returns


def covariance(asset_returns):
    cov = asset_returns.cov()
    return cov


def annualized_covariance(cov):
    annual_covariance = cov * 252
    return annual_covariance


def portfolio_variance(Covariance, weights):
    portfolio_variance = np.transpose(weights) @ Covariance @ weights
    return portfolio_variance


def portfolio_volatility(portfolio_variance):
    portfolio_volatility = np.sqrt(portfolio_variance)
    return portfolio_volatility


# Calculate the 30-day rolling window of portfolio returns
def thirty_days_rolling(portfolio_returns):
    returns_windowed = portfolio_returns.rolling(30)
    return returns_windowed


# Compute the annualized volatility series
def annualized_volatility(returns_windowed):
    volatility_series = returns_windowed.std() * np.sqrt(252)
    return volatility_series

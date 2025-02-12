import numpy as np


# Compute the portfolio's daily returns
def computepfdailyreturn(asset_prices):
    asset_returns = asset_prices.pct_change()
    return asset_returns


def portfolioreturn(asset_returns, weights):
    portfolio_returns = asset_returns.dot(weights)
    return portfolio_returns


def covariance(asset_returns):
    covariance = asset_returns.cov()
    return covariance


def annualizedcovariance(covariance):
    annual_covariance = covariance * 252
    return annual_covariance


def portfoliovariance(Covariance, weights):
    portfolio_variance = np.transpose(weights) @ Covariance @ weights
    return portfolio_variance


def portfoliovolatility(portfolio_variance):
    portfolio_volatility = np.sqrt(portfolio_variance)
    return portfolio_volatility


# Calculate the 30-day rolling window of portfolio returns
def thirtydaysrolling(portfolio_returns):
    returns_windowed = portfolio_returns.rolling(30)
    return returns_windowed


# Compute the annualized volatility series
def annualizedvolatility(returns_windowed):
    volatility_series = returns_windowed.std() * np.sqrt(252)
    return volatility_series

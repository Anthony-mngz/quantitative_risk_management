import matplotlib.pyplot as plt


# Plot portfolio's asset prices during this time
def assetpriceplot(asset_prices):
    asset_prices.plot().set_ylabel("Closing Prices, USD")
    plt.show()


def portfolioreturnsplot(portfolio_returns):
    portfolio_returns.plot().set_ylabel("Daily Return, %")
    plt.show()


# Display the covariance matrix => view
def displaycovariance(Covariance):
    print(f"Covariance={Covariance}")


def displaypfvolatility(portfolio_volatility):
    print(f"Portfolio volatility={portfolio_volatility}")


# Plot the portfolio volatility => view
def volatilityserie(volatility_series):
    volatility_series.plot().set_ylabel("Annualized Volatility, 30-day Window")
    plt.show()

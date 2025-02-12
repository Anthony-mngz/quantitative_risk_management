import matplotlib.pyplot as plt


# Plot portfolio's asset prices during this time
def asset_price_plot(asset_prices):
    asset_prices.plot().set_ylabel("Closing Prices, USD")
    plt.show()


def portfolio_returns_plot(portfolio_returns):
    portfolio_returns.plot().set_ylabel("Daily Return, %")
    plt.show()


# Display the covariance matrix
def display_covariance(Covariance):
    print(f"Covariance={Covariance}")


def display_pf_volatility(portfolio_volatility):
    print(f"Portfolio volatility={portfolio_volatility}")


# Plot the portfolio volatility
def display_volatility_serie(volatility_series):
    volatility_series.plot().set_ylabel("Annualized Volatility, 30-day Window")
    plt.show()

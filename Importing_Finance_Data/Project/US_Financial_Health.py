import pandas as pd
import pandas_datareader.data as web
from datetime import datetime
import pandas_datareader.wb as wb
import numpy as np

gold_prices = pd.read_csv("Importing_Finance_Data\\Project\\gold_prices.csv")
crude_oil_prices = pd.read_csv("Importing_Finance_Data\\Project\\crude_oil_prices.csv")

start = datetime(1999, 1, 1)
end = datetime(2019, 1, 1)

nasdaq_data = web.DataReader("NASDAQ100", "fred", start, end)
sap_data = web.DataReader("SP500", "fred", start, end)

gdp_data = wb.download(indicator="NY.GDP.MKTP.CD", country=["US"], start=start, end=end)

export_data = wb.download(indicator="NE.EXP.GNFS.CN", country=["US"], start=start, end=end)

def log_return(prices):
  return np.log(prices / prices.shift(1))

gold_returns = log_return(gold_prices["Gold_Price"])
crude_oil_returns = log_return(crude_oil_prices["Crude_Oil_Price"])
nasdaq_returns = log_return(nasdaq_data['NASDAQ100'])
sap_returns = log_return(sap_data['SP500'])
gdp_returns = log_return(gdp_data['NY.GDP.MKTP.CD'])
export_returns = log_return(export_data['NE.EXP.GNFS.CN'])

print(f"The variance of gold is {gold_returns.var()}.")
print(f"The variance of crude oil is {crude_oil_returns.var()}.")
print(f"The variance of US NASDAQ data is {nasdaq_returns.var()}.")
print(f"The variance of US S&P 500 companies is {sap_returns.var()}.")
print(f"The variance of US GDP is {gdp_returns.var()}.")
print(f"The variance of US exports is {export_returns.var()}.")

"""
The S&P 500, a collection of 500 large companies listed on stock exchanges in the United States, has the smallest variance, and thus is the least volatile. Given that the S&P 500 index is a weighted measurement of many stocks across a variety of industries, it is seen as a safer, diversified investment.

Gold, notorious for being a stable investment has the second smallest variance.

Crude oil is the most volatile, which makes sense as gas prices are often unpredictable, especially in the last 20 years.

The stocks are interesting. The NASDAQ 100 is more volatile than the S&P 500, which, when you think about it makes sense, as the S&P 500 is far more diversified and tracks more of the market.

Then finally we have GDP and exports.

Exports are very volatile, which could have to do with industries moving overseas in the last 20 years, and global competition for the production of goods.

GDP is actually fairly similar to the NASDAQ 100 in terms of volatility, which is perhaps an interesting correlation.
"""
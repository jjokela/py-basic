import pandas_datareader as pdr
import datetime
import numpy as np
import matplotlib.pyplot as plt

start = datetime.date(2010, 1, 1)
end = datetime.date(2018, 5, 1)

stock = pdr.get_data_yahoo('F', start, end)
# print(stock)
# print(stock["Adj Close"])

# print(stock["Adj Close"].pct_change())
daily_returns = stock["Adj Close"].pct_change()
daily_returns = daily_returns.dropna()
print(daily_returns)

print('std', np.std(daily_returns, ddof=1), sep=': ')
print('var', np.var(daily_returns, ddof=1), sep=': ')
print('mean', np.mean(daily_returns), sep=': ')

daily_returns.plot.hist(bins=20)
plt.show()

daily_returns.plot.hist(bins=50)
plt.show()



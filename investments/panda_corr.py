import pandas_datareader as pdr
import datetime
import numpy as np
import matplotlib.pyplot as plt

start = datetime.date(2010, 1, 1)
end = datetime.date(2018, 5, 1)

ford = pdr.get_data_yahoo('F', start, end)['Adj Close'].pct_change().dropna()
honda = pdr.get_data_yahoo('HMC', start, end)['Adj Close'].pct_change().dropna()
toyota = pdr.get_data_yahoo('TM', start, end)['Adj Close'].pct_change().dropna()

matrix = np.cov([ford, honda, toyota])
print(matrix)

print(np.corrcoef(ford, honda))

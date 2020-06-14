import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')


def read_stock_info(stock_name):
    df = pd.read_csv('CSV/' + stock_name + '.csv', parse_dates=True, index_col=0)
    # df['100ma'] = df['Close'].rolling(window=100, min_periods=0).mean()  # Takes a moving average
    df[['Open', 'Close', 'High', 'Low']].plot()
    print(df.head())

    # ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
    # ax1.plot(df.index, df['Close'])
    # ax1.plot(df.index, df['100ma'])


plt.show()

# plt.show()

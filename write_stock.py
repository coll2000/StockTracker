import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')  # chooses the method of plotting 'ggplot'

current_date = dt.datetime.today()  # gets the current date and time
last_week_date = dt.datetime.today() - dt.timedelta(days=7)  # chooses a date 7 days before current day.

print("Today's Date: ", current_date)  # prints today's date
print("This time last week: ", last_week_date)  # prints last week's date (7 days ago)


def get_currency_pairs():
    return ['GBPUSD=X',
            'EURUSD=X',
            'EURGBP=X']


def get_stock():
    return ['TSLA', 'BTC-USD']


def write_stock_info(name):
    pairs = get_currency_pairs()
    stocks = get_stock()
    if name in pairs or stocks:
        df = web.DataReader(name, 'yahoo', last_week_date, current_date)
        print(df.head())
        df.to_csv('CSV/' + name + '.csv')
    else:
        print("The code-name ", name, " is not supported at the moment.")

# write_stock_info("TSLA")

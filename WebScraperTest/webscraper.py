from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError

Start_Date = '1973-01-01'
End_Date = str(datetime.now().strftime('%Y-%m-%d'))

UK_Stock = 'TKA.DE'
USA_Stock = 'TKA.DE'


def get_stats(stock_data):
    return {
        'last': np.mean(stock_data.tail(1)),
        'short_mean_': np.mean(stock_data.tail(20)),
        'long_mean': np.mean(stock_data.tail(20)),
        'short_rolling': np.mean(stock_data.tail(20)),
        'long_rolling': np.mean(stock_data.tail(20))
    }


def clean_data(stock_data, col):
    weekdays = pd.date_range(start=Start_Date, end=End_Date)
    clean_data = stock_data[col].reindex(weekdays)
    return clean_data.fillna(method='ffill')


def create_plot(stock_data, ticker):
    stats = get_stats(stock_data)
    plt.style.use('dark_background')
    plt.subplots(figsize=(12, 8))
    plt.plot(stock_data, label=ticker)
    plt.plot(stats['short_rolling'], label='20 day rolling mean')
    plt.plot(stats['long_rolling'], label='200 day rolling mean')
    plt.xlabel('Date')
    plt.ylabel('Adj Close (p)')
    plt.legend()
    plt.title('Stock Price over Time.')

    plt.show()


def get_data(ticker):
    try:
        stock_data = data.DataReader(ticker, 'yahoo', Start_Date, End_Date)
        adj_close = clean_data(stock_data, 'Adj Close')
        create_plot(adj_close, ticker)

    except RemoteDataError:
        print('No data found for {t}')

get_data(USA_Stock)


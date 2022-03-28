# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:37:29 2018

@author: epinsky
"""
# run this  !pip install pandas_datareader
from pandas_datareader import data as web
import os
import pandas as pd
import yfinance as yf


def get_stock(ticker, start_date, end_date, s_window, l_window):
    try:
        yf.pdr_override()
        df = web.get_data_yahoo(ticker, start=start_date, end=end_date)
        df['Return'] = df['Adj Close'].pct_change()
        df['Return'].fillna(0, inplace=True)
        df['Date'] = df.index
        df['Date'] = pd.to_datetime(df['Date'])
        df['Month'] = df['Date'].dt.month
        df['Year'] = df['Date'].dt.year 
        df['Day'] = df['Date'].dt.day
        for col in ['Open', 'High', 'Low', 'Close', 'Adj Close']:
            df[col] = df[col].round(2)
        # df['Weekday'] = df['Date'].dt.weekday_name
        df['Weekday'] = df['Date'].dt.day_name()
        df['Week_Number'] = df['Date'].dt.strftime('%U')
        df['Year_Week'] = df['Date'].dt.strftime('%Y-%U')
        df['Short_MA'] = df['Adj Close'].rolling(window=s_window, min_periods=1).mean()
        df['Long_MA'] = df['Adj Close'].rolling(window=l_window, min_periods=1).mean()        
        col_list = ['Date', 'Year', 'Month', 'Day', 'Weekday', 
                    'Week_Number', 'Year_Week', 'Open', 
                    'High', 'Low', 'Close', 'Volume', 'Adj Close',
                    'Return', 'Short_MA', 'Long_MA']
        num_lines = len(df)
        df = df[col_list]
        print(f'read {num_lines} lines of data for ticker: {ticker}')
        return df
    except Exception as error:
        print(error)
        return None


def write_stock_to_file(ticker):
    try:
        input_dir = r'~/Desktop/Python/CS677/Homework/week_1_homework/'
        output_file = os.path.join(input_dir, ticker + '.csv')
        df = get_stock(ticker, start_date='2016-01-01', end_date='2020-12-31',
                       s_window=14, l_window=50)
        df.to_csv(output_file, index=False)
        print(f'wrote {str(len(df))} lines to file: {output_file}\n')
    except Exception as e:
        print(e)
        print(f'failed to get Yahoo stock data for ticker: {ticker}')


write_stock_to_file('SPY')
write_stock_to_file('HSY')

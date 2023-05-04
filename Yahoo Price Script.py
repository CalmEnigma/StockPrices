# Import libraries
import numpy as np
import pandas as pd
import os as os
import yfinance as yf
import datetime as dt
import requests
from bs4 import BeautifulSoup


# Set directory
directory = "C:\\Users\\calmp\\OneDrive\\0 - Investments\\Family"
os.chdir(directory)

# Import files
df = pd.read_excel('Family Investments.xlsx', sheet_name='Position Details')
date = pd.read_excel('Family Investments.xlsx', sheet_name='Date4Python')

# Keep relevant data
## Get the date
date = date.loc[0, 'Date']
date = date.date()

## Get the positions and tickers
df = df[['Position Name', 'Yahoo Ticker']]


# Get list of tickers
tickers = list(df['Yahoo Ticker'].dropna())

# Get prices
prices = yf.download(tickers, date, date+dt.timedelta(days=5), interval='1mo')['Open']
prices = prices.dropna()
prices = np.transpose(prices)
prices = prices.reset_index()
prices.columns = ['Yahoo Ticker', 'Price']

# Merge into df
df = df.merge(prices, on = 'Yahoo Ticker', how ='left')

# Export
df.to_csv('Yahoo Prices.csv', index=False)


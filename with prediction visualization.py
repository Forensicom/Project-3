import streamlit as st
import time
import numpy as np
import datetime
import yfinance as yf  # Import yfinance

bitcoin = yf.Ticker("BTC-USD")
ethereum = yf.Ticker("ETH-USD")
tether = yf.Ticker("USDT-USD")
ripple = yf.Ticker("XRP-USD")
binance = yf.Ticker("BNB-USD")

st.set_page_config(page_title="Analyze", page_icon="📈")

st.header("Cryptocurrency Performance Analysis")

st.write("""Go deep! Try our expert technical analysis and sentiment analysis tools below!""")

option = st.selectbox('Choose a currency to get started.', ('Bitcoin', 'Ethereum', 'Tether', 'Ripple', 'Binance'))

min_date = datetime.datetime(2010, 1, 1)
max_date = datetime.datetime(2025, 12, 12)
st.date_input("Choose the range of dates to be included in your analysis.", (min_date, max_date))

if option == "Bitcoin":
    bitcoin = yf.Ticker("BTC-USD", start=min_date, end=max_date)
elif option == "Ethereum":
    ethereum = yf.Ticker("ETH-USD", start=min_date, end=max_date)
elif option == "Tether":
    tether = yf.Ticker("USDT-USD", start=min_date, end=max_date)
elif option == "Ripple":
    ripple = yf.Ticker("XRP-USD", start=min_date, end=max_date)
elif option == "Binance":
    binance = yf.Ticker("BNB-USD", start=min_date, end=max_date)
else:
    print("oops")
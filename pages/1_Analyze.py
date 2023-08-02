# This file will hold all function to be used for analyzing a crypto currency

import streamlit as st
import time
import numpy as np
import datetime
import yfinance as yf
import pandas as pd

bitcoin = yf.Ticker("BTC-USD")
ethereum = yf.Ticker("ETH-USD")
tether = yf.Ticker("USDT-USD")
ripple = yf.Ticker("XRP-USD")
binance = yf.Ticker("BNB-USD")

st.set_page_config(page_title="Analyze", page_icon="📈")

st.sidebar.image("Resources/super_crypto.png", use_column_width =True)


# st.sidebar.header("Analyze")
st.header("Cryptocurrency Performance Analysis")

st.write("""Go deep! Try our expert technical analysis and sentinment analysis tools below!""")


option = st.selectbox('Choose a currency to get started.', ('Bitcoin', 'Ethereum', 'Tether', 'Ripple', 'Binance'))

# Just set some loose max and min data parameters.
min_date = datetime.datetime(2013,1,1)
max_date = datetime.datetime(2025,12,12)

st.date_input("Choose the range of dates to be included in your analysis.", (min_date, max_date))

if option =="Bitcoin":
        query = bitcoin.history(start=min_date, end=max_date) 
elif option =="Ethereum":
        query = ethereum.history(start=min_date, end=max_date) 
elif option == "Tether":
        query = tether.history(start=min_date, end=max_date)
elif option =="Ripple":
        query = ripple.history(start=min_date, end=max_date) 
elif option =="Binance":
        query = binance.history(start=min_date, end=max_date)
else:
    print("oops")

if st.button('Execute!'):
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)
    # api dta pull goes here
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)

query_result = pd.DataFrame(query)
query_result = query_result.drop(columns=["Dividends", "Stock Splits"])
query_result['% Change'] = query_result["Close"].pct_change() 
st.dataframe(query_result)

chart_data = query_result['Close']
st.line_chart(chart_data, use_container_width=True)


st.write("""Here is where we will put a chart that shows the predicted yhat values""")

st.write("""Here is where we will put the output from our tweepy sentinment analysis.""")
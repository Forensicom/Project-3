import streamlit as st
import yfinance as yf
import feedparser
import webbrowser
import pandas as pd
import requests

st.set_page_config(page_title="Home")

bitcoin = yf.Ticker("BTC-USD")
ethereum = yf.Ticker("ETH-USD")
tether = yf.Ticker("USDT-USD")
ripple = yf.Ticker("XRP-USD")
binance = yf.Ticker("BNB-USD")

btc_url = "https://api.coincap.io/v2/assets/bitcoin"
eth_url = "https://api.coincap.io/v2/assets/ethereum"
usdt_url = "https://api.coincap.io/v2/assets/tether"
xrp_url = "https://api.coincap.io/v2/assets/xrp"
bnb_url = "https://api.coincap.io/v2/assets/binance-usd"

col1, col2, col3 = st.columns([7,2,2])

st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 150px !important; # Set the width to your desired value
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.image("Resources/super_crypto.png", use_column_width =True)


with col1:
    crypto_logos = st.image(["https://cryptologos.cc/logos/bitcoin-btc-logo.png?v=025", 
                            "https://cryptologos.cc/logos/ethereum-eth-logo.png?v=025", 
                            "https://cryptologos.cc/logos/tether-usdt-logo.png?v=025", 
                            "https://cryptologos.cc/logos/xrp-xrp-logo.png?v=025", 
                            "https://cryptologos.cc/logos/bnb-bnb-logo.png?v=025"], width =50)
                  

col1.write("<h1 style= 'text-align: center'>Welcome to Super Crypto!</h1>", unsafe_allow_html=True)


                  
col1.markdown("""
This platform enables users to both analyze and trade the top 5 crpyto currencies by market cap.
They are Bitcoin, Ethereum, Tether, Binance and Ripple. 
Not only can users perform the basic technical analysis of a crypto currency, 
they will see a predictive analysis of each crypto and we have also added a sentimment analysis capability to the platform. 
Users can get a feel for the mood of the pubilc around th ecrpyto of their choice. 
We do this by analyzing Tweets and producing a categorized output..
""")
# **************************************************************************************************
# NEED HELP HERE WITH STR VS FLOAT ERROR
# **************************************************************************************************
leader = 0

source_dict={'btc': btc_url, 
'eth': eth_url, 
'usdt': usdt_url, 
'xrp': xrp_url, 
'bnb': bnb_url}

data_dict={}

for coin in source_dict: 
    data=requests.get(source_dict[coin]).json()
    data_dict[coin]=float(data['data']['changePercent24Hr'])

st.write(data_dict)
# btc_data=
# btc_pct = btc_data['data']['changePercent24Hr']
# eth_pct = eth_url(['data']['changePercent24Hr'])
# usdt_pct = usdt_url(['data']['changePercent24Hr'])
# xrp_pct = xrp_url(['data']['changePercent24Hr'])
# bnb_pct = bnb_url(['data']['changePercent24Hr'])

with col1:
    if btc_pct > 0:
        leader == btc_pct
        st.write('Yesterdays highest performer was Bitcoin with an',leader,'% change.')
    elif eth_pct > leader:
        leader == eth_pct
        st.write('Yesterdays highest performer was Ethereum with an',leader,'% change.')
    elif usdt_pct > leader:
        leader == usdt_pct
        st.write('Yesterdays highest performer was Tether with an',leader,'% change.')
    elif xrp_pct > leader:
        leader == xrp_pct
        st.write('Yesterdays highest performer was Ripple with an',leader,'% change.')
    elif bnb_pct > leader:
        leader == bnb_pct
        st.write('Yesterdays highest performer was Binance with an',leader,'% change.')
    else:
        st.write('Bad day for crypto yesterday. Every coin lost.')

# *****************************************************************************************************
# This is the current position of every coin we track
# Code works
# Need to change order of columns
# *****************************************************************************************************
    bitcoin_day = bitcoin.history(period="1d")
    bitcoin_day_df = pd.DataFrame(bitcoin_day)
    bitcoin_day_df = bitcoin_day_df.drop(columns=["Dividends", "Stock Splits"])
    bitcoin_chg = bitcoin.history(period="2d")
    bitcoin_day_df['% Change'] = bitcoin_chg["Close"].pct_change() 
    bitcoin_day_df['Coin'] = "Bitcoin"

    ethereum_day = ethereum.history(period="1d")
    ethereum_day_df = pd.DataFrame(ethereum_day)
    ethereum_day_df = ethereum_day_df.drop(columns=["Dividends", "Stock Splits"])
    ethereum_chg = ethereum.history(period="2d")
    ethereum_day_df['% Change'] = ethereum_chg["Close"].pct_change() 
    ethereum_day_df['Coin'] = "Ethereum"

    tether_day = tether.history(period="1d")
    tether_day_df = pd.DataFrame(tether_day)
    tether_day_df = tether_day_df.drop(columns=["Dividends", "Stock Splits"])
    tether_chg = tether.history(period="2d")
    tether_day_df['% Change'] = tether_chg["Close"].pct_change() 
    tether_day_df['Coin'] = "Tether"

    ripple_day = ripple.history(period="1d")
    ripple_day_df = pd.DataFrame(ripple_day)
    ripple_day_df = ripple_day_df.drop(columns=["Dividends", "Stock Splits"])
    ripple_chg = ripple.history(period="2d")
    ripple_day_df['% Change'] = ripple_chg["Close"].pct_change() 
    ripple_day_df['Coin'] = "Ripple"

    binance_day = binance.history(period="1d")
    binance_day_df = pd.DataFrame(binance_day)
    binance_day_df = binance_day_df.drop(columns=["Dividends", "Stock Splits"])
    binance_chg = binance.history(period="2d")
    binance_day_df['% Change'] = binance_chg["Close"].pct_change() 
    binance_day_df['Coin'] = "Binance"

    all_coins_df = pd.DataFrame()
    all_coins_df= pd.concat([bitcoin_day_df,  ethereum_day_df, tether_day_df, ripple_day_df, binance_day_df],axis="rows", join="outer")
    st.write(all_coins_df)

# ***********************************************************************************
# Column 3 is reserved for the RSS Feed content
# ***********************************************************************************

with col3:
    st.markdown('NEWS')
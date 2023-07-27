import streamlit as st
import yfinance as yf
import requests
import os
import json

api_key = os.getenv("COINCAP_API_KEY")

st.set_page_config(page_title="Transact")

st.sidebar.image("Resources/super_crypto.png", use_column_width =True)

btc_url = "https://api.coincap.io/v2/assets/bitcoin"
eth_url = "https://api.coincap.io/v2/assets/ethereum"
usdt_url = "https://api.coincap.io/v2/assets/tether"
xrp_url = "https://api.coincap.io/v2/assets/xrp"
bnb_url = "https://api.coincap.io/v2/assets/binance-usd"

# create a two column page. Firs tcolumn will be BUY. Second column will be SELL.
col1, col2 = st.columns(2)

transaction = st.radio("Please choose a transaction type",('Buy', 'Sell'))
if transaction =='Buy':
    print (f'Pick the crypto you want to buy')
elif transaction == 'Sell':
    print (f'Pick the crypto you want to sell') 
else:
    print("Error")
    
options = ['Bitcoin', 'Ethereum', 'Tether', 'Ripple', 'Binance']
choice = st.selectbox('Choose a cryptocurrency to get started.', options)
#Good place for an IF statement
if choice == "Bitcoin":
    output = requests.get(btc_url).json()
elif choice == "Ethereum":
    output = requests.get(eth_url).json()
elif choice == "Tether":
    output = requests.get(usdt_url).json()
elif choice == "Ripple":
    output = requests.get(xrp_url).json()
elif choice == "Binance":
    output = requests.get(bnb_url).json()
else: 
    print("Pick something!!")
    
# Grabbing the current price in USD
now_price = output['data']['priceUsd']
print(now_price)

amt = st.number_input("Amount",format="%.2f")
value = now_price * amt
print(value)
st.write('Confirmation of transaction goes down here')


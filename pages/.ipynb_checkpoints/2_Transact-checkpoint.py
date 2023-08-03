import streamlit as st
import yfinance as yf
import requests
import os
import json
from decimal import Decimal

st.set_page_config(page_title="Transact")

st.sidebar.image("Resources/super_crypto.png", use_column_width =True)

cash_balance = 1000

btc_url = "https://api.coincap.io/v2/assets/bitcoin"
eth_url = "https://api.coincap.io/v2/assets/ethereum"
usdt_url = "https://api.coincap.io/v2/assets/tether"
xrp_url = "https://api.coincap.io/v2/assets/xrp"
bnb_url = "https://api.coincap.io/v2/assets/binance-usd"

options = ['Bitcoin', 'Ethereum', 'Tether', 'Ripple', 'Binance']
st.markdown('### Buy and Sell Cryptocurrency')
# with st.form("inputs_form"):
transaction = st.radio("Please choose a transaction type",('Buy', 'Sell'))
if transaction == 'Sell':
    to_wallet = st.text_input("Enter the destination Wallet ID")
else:
    wallet = st.text_input("Enter your Wallet ID")
    choice = st.selectbox('Choose a cryptocurrency to get started.', options)
    amt = st.number_input("Amount")
#    if st.form_submit_button("Execute!"):
#       st.write("Transaction launched")
        
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

'''
    # Once a crpyto is chosen we also need to calculate how muchof that particular crpyto the user owns. We will print it out in a statement after they make the selection.

    # Grabbing the current price in USD
    now_price = output['data']['priceUsd']
    now_price = Decimal(now_price)
    print(now_price)

   
    amt = Decimal(amt)


        value = now_price * amt
        print(value)

st.write('Confirmation of transaction goes down here')

'''
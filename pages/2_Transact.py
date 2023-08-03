import streamlit as st
import yfinance as yf
import requests
import os
import json
from decimal import Decimal

st.set_page_config(page_title="Transact",page_icon=":heavy_dollar_sign:")

st.sidebar.image("Resources/super_crypto.png", use_column_width =True)

cash_balance = 1000

btc_url = "https://api.coincap.io/v2/assets/bitcoin"
eth_url = "https://api.coincap.io/v2/assets/ethereum"
usdt_url = "https://api.coincap.io/v2/assets/tether"
xrp_url = "https://api.coincap.io/v2/assets/xrp"
bnb_url = "https://api.coincap.io/v2/assets/binance-usd"

options = ['Bitcoin', 'Ethereum', 'Tether', 'Ripple', 'Binance']
st.markdown('### Buy and Sell Cryptocurrency')
with st.form("inputs_form"):
    transaction = st.radio("Please choose a transaction type",('Buy', 'Sell'))
    wallet = st.text_input("Enter your Wallet ID")
    to_walt = st.text_input("Enter the destination Wallet ID")
    choice = st.selectbox('Choose a cryptocurrency to get started.', options)
    amt = st.number_input("Amount")
    st.form_submit_button('Execute!')

 
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

st.write("Users that try to buy or sell outside of their limitations will be thrown an error and the transaction will not proceed.")

   
import streamlit as st
import yfinance as yf

# The purpose of this page is to help users calulate how much of a crypto they could buy for X dollars.
# This will require the CURREN tprice of whatever crypto they select. 

st.set_page_config(page_title="Calculator")

st.sidebar.image("Resources/super_crypto.png", use_column_width =True)

st.markdown("""## Conversion Calculator""")

amt = st.number_input("Amount to convert")
from_opt = st.selectbox('Convert', ('USD','Bitcoin', 'Ethereum', 'Tether', 'Ripple', 'Binance'))
to_opt = st.selectbox('To', ('USD', 'Bitcoin', 'Ethereum', 'Tether', 'Ripple', 'Binance'))
from_price = 0
to_price = 0

btc_url = "https://api.coincap.io/v2/assets/bitcoin"
eth_url = "https://api.coincap.io/v2/assets/ethereum"
usdt_url = "https://api.coincap.io/v2/assets/tether"
xrp_url = "https://api.coincap.io/v2/assets/xrp"
bnb_url = "https://api.coincap.io/v2/assets/binance-usd"

if from_opt =="Bitcoin":
        from_price = btc_url['data']['priceUsd']
elif from_opt =="USD":
        from_price = 1
elif from_opt =="Ethereum":
        from_price = eth_url['data']['priceUsd']
elif from_opt == "Tether":
        from_price = udt_url['data']['priceUsd']
elif from_opt =="Ripple":
        from_price = xrp_url['data']['priceUsd']
elif from_opt =="Binance":
        from_price = bnb_url['data']['priceUsd']
else:
    print("oops")

if to_opt =="Bitcoin":
        to_price = btc_url['data']['priceUsd']
elif to_opt == "USD":
        to_price = 1
elif to_opt =="Ethereum":
        to_price = eth_url['data']['priceUsd']
elif to_opt == "Tether":
        to_price = udt_url['data']['priceUsd']
elif to_opt =="Ripple":
        to_price = xrp_url['data']['priceUsd']
elif to_opt =="Binance":
        to_price = bnb_url['data']['priceUsd']
else:
    print("oops")

calculated = ((amt*from_price)/ to_price)
st.write(calculated)

'''
with col1:
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
'''
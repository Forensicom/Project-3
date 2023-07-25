import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Transact")

st.sidebar.image("Resources/super_crypto.png", use_column_width =True)






# create a two column page. Firs tcolumn will be BUY. Second column will be SELL.

col1, col2 = st.columns(2)

transaction = st.radio("Please choose a transaction type",('Buy', 'Sell'))

options = ['Bitcoin', 'Ethereum', 'Tether', 'Ripple', 'Binance']
choice = st.selectbox('Choose a cryptocurrency to get started.', options)
#Good place for an IF statement
if choice == "Bitcoin":
    rate = (yf.Ticker("BTC-USD").info['regularMarketPreviousClose'])
elif choice =="Ethereum":
    rate = (yf.Ticker("ETH-USD").info['regularMarketPreviousClose'])
elif choice =="Tether":
    rate = (yf.Ticker("USDT-USD").info['regularMarketPreviousClose'])
elif choice =="Ripple":
    rate = (yf.Ticker("XRP-USD").info['regularMarketPreviousClose'])
elif choice =="Binance":
    rate = (yf.Ticker("BNB-USD").info['regularMarketPreviousClose'])
else:
    print("Pick one!")

amt = st.number_input("Amount")
value = rate * amt
print(value)
st.write('Confirmation of transaction goes down here')

    # We need to pull the CURRENT PRICE of the crypto when it is chosen: yf.ticker(transact_coin)

    
import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Transact")

st.sidebar.image("Resources/super_crypto.png", use_column_width =True)

# This app will include functions used to perform a crypto currency transaction.

# create a two column page. Firs tcolumn will be BUY. Second column will be SELL.

col1, col2 = st.columns(2)

with col1:
    st.write("""BUY""")
    st.selectbox('Choose a currency to get started.', ('Bitcoin', 'Ethereum', 'Tether', 'Ripple', 'Binance'))
    st.number_input("Amount to purchase")
    st.write('Confirmation of transaction goes down here')

with col2:
    st.write("""SELL""")
    st.selectbox('Choose a crypto currency', ('Bitcoin', 'Ethereum', 'Tether', 'Ripple', 'Binance'))
    st.number_input("Amount to sell") # add an action onchange
    st.write('Confirmation of transaction goes down here') #success triggers st.balloons()

    
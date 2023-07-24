import streamlit as st
import yfinance as yf

# The purpose of this page is to help users calulate how much of a crypto they could buy for X dollars.
# This will require the CURREN tprice of whatever crypto they select. 

st.set_page_config(page_title="Calculator")

st.sidebar.image("Resources/super_crypto.png", use_column_width =True)

st.markdown("""## Conversion Calculator""")


st.selectbox('Convert', ('USD','Bitcoin', 'Ethereum', 'Tether', 'Ripple', 'Binance'))

st.selectbox('To', ('USD', 'Bitcoin', 'Ethereum', 'Tether', 'Ripple', 'Binance'))
st.write("")
st.number_input("Amount to convert")
# converter = yf()


# from_currency = 
# to_currency =

def convert_currency(amount, from_currency, to_currency):
    try:
        rate = converter.get_rate(from_currency, to_currency)
        converted_amount = round(amount * rate, 2)
        return converted_amount
    except :
        st.write(f"<h3>Error: Cannot find the rate.</h3>",unsafe_allow_html=True)
        return None

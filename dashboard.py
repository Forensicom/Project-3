import yfinance as yf
import streamlit as st
from PIL import Image
from urllib.request import urlopen


st.title("Cryptocurrency daily prices")
st.header("Main Dashboard")
st.subheader("You can add more crypto in code")

Bitcoin = 'BTC-USD'
Etherium = 'ETH-USD'
Ripple = 'XRP-USD'
BitcoinCash = "BCH-USD"

BTC_Data = yf.Ticker(Bitcoin)
Eth_Data = yf.Ticker(Etherium)
XRP_Data = yf.Ticker(Ripple)
BCH_Data = yf.Ticker(BitcoinCash)

#Fetch history data from yahoo finance

BTCHis = BTC_Data.history(period="max")
ETHHis = Eth_Data.history(period="max")
XRPHis = XRP_Data.history(period="max")
BCHHis = BCH_Data.history(period="max")

#Fetch crypto data for dataframe
BTC = yf.download(Bitcoin, start="2023-07-21", end="2023-07-22")
ETH = yf.download(Etherium, start="2023-07-21", end="2023-07-22")
XRP = yf.download(Ripple, start="2023-07-21", end="2023-07-22")
BCH = yf.download(BitcoinCash, start="2023-07-21", end="2023-07-22")

#Bitcoin
st.write("BITCOIN($)")
imageBTC= Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
st.image(imageBTC)
st.table(BTC)
#Display a chart
st.bar_chart(BTCHis.Close)

#Etherium
st.write("Etherium($)")
imageETH= Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))
st.image(imageETH)
st.table(ETH)
#Display a chart
st.bar_chart(ETHHis.Close)

#Ripple
st.write("Ripple($)")
imageXRP= Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/52.png'))
st.image(imageXRP)
st.table(XRP)
#Display a chart
st.bar_chart(XRPHis.Close)

#BitcoinCash
st.write("Bitcoin Cash($)")
imageBCH= Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png'))
st.image(imageBCH)
st.table(BCH)
#Display a chart
st.bar_chart(BCHHis.Close)

option = st.selectbox('CryptoCurrecies',('Bitcoin', 'Etherium', 'Ripple'))
st.write('Your currency graph', st.bar_chart)
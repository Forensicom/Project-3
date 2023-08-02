import streamlit as st
import yfinance as yf
import feedparser
import webbrowser

st.set_page_config(page_title="Super Crypto")

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
We do this by analyzing Tweets and producing a caetogirze doutput..
""")


leader = 0

with col1:
    if btc_url['data']['changePercent24Hr'] > 0:
        leader == btc_url['data']['changePercent24Hr']
        st.write('Yesterdays highest performer was Bitcoin with an',leader,'% change.')
    elif eth_url['data']['changePercent24Hr'] > leader:
        leader == eth_url['data']['changePercent24Hr']
        st.write('Yesterdays highest performer was Ethereum with an',leader,'% change.')
    elif usdt_url['data']['changePercent24Hr'] > leader:
        leader == usdt_url['data']['changePercent24Hr']
        st.write('Yesterdays highest performer was Tether with an',leader,'% change.')
    elif xrp_url['data']['changePercent24Hr'] > leader:
        leader == xrp_url['data']['changePercent24Hr']
        st.write('Yesterdays highest performer was Ripple with an',leader,'% change.')
    elif bnb_url['data']['changePercent24Hr'] > leader:
        leader == bnb_url['data']['changePercent24Hr']
        st.write('Yesterdays highest performer was Binance with an',leader,'% change.')
    else:
        st.write('Bad day for crypto yesterday. Every coin lost.')

    
col1.markdown("""### Insert Pandas Dataframe with one row for each crpyto (contains open.close.high,low.volume.pct_change """)



with col3:
    st.markdown('NEWS')
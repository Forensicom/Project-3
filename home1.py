import streamlit as st
import yfinance as yf
import feedparser
import webbrowser
import pandas as pd
import openpyxl
import numpy as np
from IPython.core.display import display, HTML

st.set_page_config(page_title="Group 4")



bitcoin = yf.Ticker("BTC-USD")
ethereum = yf.Ticker("ETH-USD")
tether = yf.Ticker("USDT-USD")
ripple = yf.Ticker("XRP-USD")
binance = yf.Ticker("BNB-USD")

col1, col2 = st.columns([12,9])

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

col1.markdown("""### Insert Line Graph showing yesterdays top performing cryptocurrency goes here (plot price for every minute yesterday.""")
col1.button("Re-run")

col1.markdown("""### Insert Pandas Dataframe with one row for each crpyto (contains open.close.high,low.volume.pct_change """)

with col2:
    col2.markdown("<h4 style= 'text-align: center'>NEWS</h4>", unsafe_allow_html=True)
    #col2.write("This is where we will put the RSS feed")
    feed = feedparser.parse("https://cointelegraph.com/rss")
    feed_title = feed['feed']['title']
    feed_entries = feed.entries
    for entry in feed.entries:
       article_title = entry.title
       article_link = entry.link
    #df = pd.DataFrame(feed_entries, columns=["Crypto", "link"])
    data = {}
    for entry in feed.entries:
        #data.setdefault("Crypto",[])
        #data.setdefault("link",[])
        data.setdefault("Crypto News",[])
        #data["Crypto"].append(entry.title)
        #data["link"].append(entry.link)
        data["Crypto News"].append(f'<a href = "{entry.link}">{entry.title}</a>')

    st.write(pd.DataFrame(data).to_html(escape=False, index=False), unsafe_allow_html = True)
    '''
    st.dataframe(data,750
                 , column_config = {
                     "link": st.column_config.LinkColumn (
                         "news feed", max_chars= 999 )
                         }
                         ) 
                    '''  

         

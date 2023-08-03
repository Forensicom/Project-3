import streamlit as st
import yfinance as yf


st.set_page_config(page_title="Portfolio",page_icon="	:rocket:")
st.sidebar.image("Resources/super_crypto.png", use_column_width =True)

st.markdown('## My Portfolio')

st.write('Users will be able to see their current holdings in a single dataframe here.')
         
st.write('A summary of the investment performance will also be available.')

st.write('Finally, down here we want a dataframe that details every transaction made by the user. It will serve as the support documentation they will require for tax reporting purposes.')
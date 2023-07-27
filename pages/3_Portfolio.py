# This python app will include individual functions that can display everything a user would want to know about their portfolio.

# Examples of data to show the user include:

# FUNCTION: "currentstatus" - Creates a pandas dataframe. Includes the names of the crypto currencies held, amount of the currency owned, percent_change in value over ownership period, total current value in USD. 

# FUNCTION: "cashPosition" - Shows the amount of USD cash on hand right now.

# FUNCTION: "overallPosition" - Overall percentage of gain or loss. Put GAIN in green numbers. Loss should be in RED. We will use Streamlit to highlight this output on the portfolio page.

# FUNCTION: "activityHistory" - This function produces a pandas dataframe that includes the date/time of every transaction made by the user. Details should include date/time of transaction, name of crypto purchased, amount purchased, total cost of purchase.

# A date/time that shows when the report was produced.

# st.sidebar.header("My Portfolio")

import streamlit as st
import yfinance as yf

cash_balance = mycash # cash variable is used here and on the analyze page. Need to write a get_balance() function.

st.set_page_config(page_title="Portfolio")
st.sidebar.image("Resources/super_crypto.png", use_column_width =True)

st.markdown("""## My Portfolio""")
st.write('Right in the middle of the top of this page we will put the users total % portfolio gain or loss in large font')
         
st.write('We want to show details of the users crypto holdings as well as their remaining cash')

st.write('Finally, down here we want a dataframe that details every transaction made by the user. It should include date/time amount spent/amount purchased/ currentvalue/%change')
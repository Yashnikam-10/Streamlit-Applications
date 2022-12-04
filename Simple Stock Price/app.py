import streamlit as st
import yfinance as yf
import pandas as pd

st.write(""" 
# Stock Price

The opening and closing Stock Prices of Google

""")

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-05-20', end = '2022-10-20')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
import streamlit as st
import sys

sys.path.append('/home/geetheswar/Documents/projects/ChatMate')
from stocks.predictor import *

st.title('Stock Forecast App')

stocks = ('GOOG', 'AAPL', 'MSFT', 'TCS', 'INFY')
selected_stock = st.selectbox('Select dataset for prediction', stocks)


@st.cache_data
def get_data(ticker):
    return load_data(ticker)

data = get_data(selected_stock)

st.subheader('Stock Values')
st.write(data, unsafe_allow_html=True)

st.plotly_chart(plot_data(data))

m = model(data)
forecast = get_forecast_data(m, 365)

# Show and plot forecast
st.subheader('Forecast data')
st.write(forecast.tail())

st.write(f'Forecast plot for 1 years')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast components")
fig2 = m.plot_components(forecast)
st.write(fig2)

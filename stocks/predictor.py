import yfinance as yf

from datetime import date
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as goj

START = "2017-01-01"
END = date.today().strftime("%Y-%m-%d")
print(END)

stock = "GOOG"


def load_data(ticker):
    data = yf.download(ticker, START, END)
    data.reset_index(inplace=True)
    return data


def plot_data(data):
    fig = goj.Figure()
    fig.add_trace(goj.Scatter(x=data['Date'], y=data['Open'], name='Stock Opening'))
    fig.add_trace(goj.Scatter(x=data['Date'], y=data['Close'], name='Stock Closing'))
    fig.layout.update(title_text="Stocks Data", xaxis_rangeslider_visible=True)
    return fig


def model(data):
    df_train = data[['Date', 'Close']]
    df_train = df_train.rename(columns={'Date': 'ds', 'Close': 'y'})

    m = Prophet()
    m.fit(df_train)
    return m


def get_forecast_data(model, period):
    future = model.make_future_dataframe(periods=period)
    forcast = model.predict(future)
    return forcast

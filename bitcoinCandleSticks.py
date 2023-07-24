from pycoingecko import CoinGeckoAPI
import plotly.graph_objects as go
import pandas as pd

cg = CoinGeckoAPI()

bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days = 30)
bitcoin_data_prices = bitcoin_data['prices']

data = pd.DataFrame(bitcoin_data_prices, columns=['TimeStamp','Price'])
data["Date"] = pd.to_datetime(data['TimeStamp'], unit='ms')

candlestick_data = data.groupby(data.Date.dt.date).agg({'Price':['min','max','first','last']})

fig = go.Figure(data=[go.Candlestick(x=candlestick_data.index,
                                     open=candlestick_data['Price']['first'],
                                     high=candlestick_data['Price']['max'],
                                     low=candlestick_data['Price']['min'],
                                     close=candlestick_data['Price']['last'],
                                     )])
fig.update_layout(title='Bitcoin', xaxis_title='Date', yaxis_title = 'Prices')

fig.show()


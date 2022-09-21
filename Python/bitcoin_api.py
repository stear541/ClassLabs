!pip install pycoingecko
!pip install plotly
!pip install mplfinance

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc

#create a dictionary
dict_={'a':[11,21,31],'b':[12,22,32]}

df=pd.DataFrame(dict_)
type(df)

df.head()

df.mean()

#begin the lab
cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)

type(bitcoin_data )  #dict

bitcoin_price_data = bitcoin_data['prices']

bitcoin_price_data[0:5]
'''
 [[1656784869614, 19301.028057785716],
 [1656788499021, 19311.849496405244],
 [1656792059970, 19257.767867548453],
 [1656795730976, 19271.764100980385],
 [1656799366832, 19378.141016164303]]
 '''
 
 #turn data into a pandas dataframe
 data = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp', 'Price'])
 
 #convert timestamp
 data['date'] = data['TimeStamp'].apply(lambda d: datetime.date.fromtimestamp(d/1000.0))

 #using modified date, find min max open and close for candlesticks
 candlestick_data = data.groupby(data.date, as_index=False).agg({"Price": ['min', 'max', 'first', 'last']})
 
 #use plotly to create candlestick chart
 fig = go.Figure(data=[go.Candlestick(x=candlestick_data['date'],
                open=candlestick_data['Price']['first'], 
                high=candlestick_data['Price']['max'],
                low=candlestick_data['Price']['min'], 
                close=candlestick_data['Price']['last'])
                ])

fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()
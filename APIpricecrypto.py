#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


def get_binance_price(crypto_symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={crypto_symbol}USDT"
    response = requests.get(url)
    data = response.json()
    return data['price']


# In[3]:


def get_coinbase_price(crypto_symbol):
    url = f"https://api.coinbase.com/v2/prices/{crypto_symbol}-USD/spot"
    response = requests.get(url)
    data = response.json()
    return data['data']['amount']


# In[4]:


def get_kraken_price(crypto_symbol):
    pair_symbol = "XBTUSD" if crypto_symbol == "BTC" else f"{crypto_symbol}USD"
    url = f"https://api.kraken.com/0/public/Ticker?pair={pair_symbol}"
    response = requests.get(url)
    data = response.json()
    return data['result'][f'X{crypto_symbol}ZUSD']['c'][0]


# In[5]:


def get_bitfinex_price(crypto_symbol):
    url = f"https://api-pub.bitfinex.com/v2/tickers?symbols=t{crypto_symbol}USD"
    response = requests.get(url)
    data = response.json()
    return data[0][7]


# In[6]:


def get_huobi_price(crypto_symbol):
    url = f"https://api.huobi.pro/market/trade?symbol={crypto_symbol.lower()}usdt"
    response = requests.get(url)
    data = response.json()
    return data['tick']['data'][0]['price']


# In[7]:


def get_gemini_price(crypto_symbol):
    url = f"https://api.gemini.com/v1/pubticker/{crypto_symbol.lower()}usd"
    response = requests.get(url)
    data = response.json()
    return data['last']


# In[8]:


def get_kucoin_price(crypto_symbol):
    url = f"https://api.kucoin.com/api/v1/market/orderbook/level1?symbol={crypto_symbol}-USDT"
    response = requests.get(url)
    data = response.json()
    return data['data']['price']


# In[9]:


def get_bitstamp_price(crypto_symbol):
    url = f"https://www.bitstamp.net/api/v2/ticker/{crypto_symbol.lower()}usd/"
    response = requests.get(url)
    data = response.json()
    return data['last']


# In[10]:


def get_gateio_price(crypto_symbol):
    url = f"https://data.gate.io/api2/1/ticker/{crypto_symbol.lower()}_usdt"
    response = requests.get(url)
    data = response.json()
    return data['last']


# In[11]:


def get_bitmex_price(crypto_symbol):
    url = f"https://www.bitmex.com/api/v1/instrument?symbol={crypto_symbol}USD&count=1&reverse=true"
    response = requests.get(url)
    data = response.json()
    return data[0]['lastPrice']


# In[12]:


def get_exmo_price(crypto_symbol):
    url = "https://api.exmo.com/v1/ticker/"
    response = requests.get(url)
    data = response.json()
    return data[f'{crypto_symbol}_USD']['last_trade']


# In[13]:


def get_cexio_price(crypto_symbol):
    url = f"https://cex.io/api/last_price/{crypto_symbol}/USD"
    response = requests.get(url)
    data = response.json()
    return data['lprice']


# In[ ]:





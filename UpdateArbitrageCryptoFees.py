#!/usr/bin/env python
# coding: utf-8

# In[13]:


#!/usr/bin/env python
# coding: utf-8

# API FILES

import requests
import matplotlib.pyplot as plt

# Fonction pour récupérer les prix des différentes cryptomonnaies sur différents échanges
def get_price(exchange, symbol):
    urls = {
        "binance": f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}USDT",
        "coinbase": f"https://api.coinbase.com/v2/prices/{symbol}-USD/spot",
        "kraken": f"https://api.kraken.com/0/public/Ticker?pair={symbol}USD",
        "bitfinex": f"https://api-pub.bitfinex.com/v2/tickers?symbols=t{symbol}USD",
        "huobi": f"https://api.huobi.pro/market/trade?symbol={symbol.lower()}usdt",
        "gemini": f"https://api.gemini.com/v1/pubticker/{symbol.lower()}usd",
        "kucoin": f"https://api.kucoin.com/api/v1/market/orderbook/level1?symbol={symbol}-USDT",
        "bitstamp": f"https://www.bitstamp.net/api/v2/ticker/{symbol.lower()}usd/",
        "gateio": f"https://data.gate.io/api2/1/ticker/{symbol.lower()}_usdt",
        "bitmex": f"https://www.bitmex.com/api/v1/instrument?symbol={symbol}USD&count=1&reverse=true",
        "exmo": f"https://api.exmo.com/v1/ticker/"
    }
    url = urls.get(exchange)
    response = requests.get(url)
    data = response.json()
    
    if exchange == "binance":
        return float(data['price'])
    elif exchange == "coinbase":
        return float(data['data']['amount'])
    elif exchange == "kraken":
        return float(data['result'][f'X{symbol}ZUSD']['c'][0])
    elif exchange == "bitfinex":
        return float(data[0][7])
    elif exchange == "huobi":
        return float(data['tick']['data'][0]['price'])
    elif exchange == "gemini":
        return float(data['last'])
    elif exchange == "kucoin":
        return float(data['data']['price'])
    elif exchange == "bitstamp":
        return float(data['last'])
    elif exchange == "gateio":
        return float(data['last'])
    elif exchange == "bitmex":
        return float(data[0]['lastPrice'])
    elif exchange == "exmo":
        return float(data[f'{symbol}_USD']['last_trade'])

# MAIN PROGRAM

# Liste des cryptomonnaies à analyser
cryptos = ["BTC", "ETH", "WIF"]

# Liste des échanges à analyser
exchanges = ["binance", "coinbase", "kraken", "bitfinex", "huobi", "gemini", "kucoin", "bitstamp", "gateio", "bitmex", "exmo"]

# Taux de frais par plateforme (en pourcentage)
fees = {
    "binance": {"maker": 0.1, "taker": 0.1},
    "coinbase": {"maker": 0.5, "taker": 0.5},
    "kraken": {"maker": 0.16, "taker": 0.26},
    "bitfinex": {"maker": 0.1, "taker": 0.2},
    "huobi": {"maker": 0.2, "taker": 0.2},
    "gemini": {"maker": 0.35, "taker": 0.35},
    "kucoin": {"maker": 0.1, "taker": 0.1},
    "bitstamp": {"maker": 0.5, "taker": 0.5},
    "gateio": {"maker": 0.2, "taker": 0.2},
    "bitmex": {"maker": -0.025, "taker": 0.075},
    "exmo": {"maker": 0.2, "taker": 0.2}
}

# Liens pour les échanges
exchange_links = {
    "binance": "https://www.binance.com/en/trade/{symbol}_USDT",
    "coinbase": "https://www.coinbase.com/price/{symbol}",
    "kraken": "https://www.kraken.com/prices/{symbol}",
    "bitfinex": "https://www.bitfinex.com/t/{symbol}:USD",
    "huobi": "https://www.huobi.com/en-us/exchange/{symbol}_usdt",
    "gemini": "https://www.gemini.com/prices/{symbol}",
    "kucoin": "https://www.kucoin.com/trade/{symbol}-USDT",
    "bitstamp": "https://www.bitstamp.net/markets/{symbol}usd/",
    "gateio": "https://www.gate.io/trade/{symbol}_usdt",
    "bitmex": "https://www.bitmex.com/app/trade/{symbol}",
    "exmo": "https://exmo.com/en/trade/{symbol}_USD"
}

# Récupération des prix pour chaque cryptomonnaie sur chaque échange
prices = {crypto: {} for crypto in cryptos}
for crypto in cryptos:
    for exchange in exchanges:
        try:
            price = get_price(exchange, crypto)
            prices[crypto][exchange] = price
        except Exception as e:
            print(f"Erreur lors de la récupération du prix pour {crypto} sur {exchange}: {e}")

# Affichage des prix obtenus
for crypto in cryptos:
    print(f"Prix pour {crypto}:")
    for exchange in exchanges:
        print(f"{exchange.capitalize()}: {prices[crypto].get(exchange, 'N/A')}")

# Calcul des spreads et prise en compte des frais
arbitrage_opportunities = []
for crypto in cryptos:
    min_exchange = min(prices[crypto], key=prices[crypto].get)
    max_exchange = max(prices[crypto], key=prices[crypto].get)
    min_price = prices[crypto][min_exchange]
    max_price = prices[crypto][max_exchange]

    # Frais pour l'achat et la vente
    fee_buy = fees[min_exchange]['taker'] / 100
    fee_sell = fees[max_exchange]['maker'] / 100

    # Coût d'achat et revenu de vente ajustés pour les frais
    cost_buy = min_price * (1 + fee_buy)
    revenue_sell = max_price * (1 - fee_sell)

    # Calcul du profit net après frais
    profit_net = revenue_sell - cost_buy

    if profit_net > 0:
        opportunity = {
            "crypto": crypto,
            "buy_exchange": min_exchange,
            "buy_price": min_price,
            "sell_exchange": max_exchange,
            "sell_price": max_price,
            "profit": profit_net
        }
        arbitrage_opportunities.append(opportunity)
        buy_url = exchange_links[min_exchange].format(symbol=crypto.lower())
        sell_url = exchange_links[max_exchange].format(symbol=crypto.lower())
        print(f"Arbitrage Opportunity for {crypto}!")
        print(f"Buy on {min_exchange} at {min_price} USD. Link: {buy_url}")
        print(f"Sell on {max_exchange} at {max_price} USD. Link: {sell_url}")
        print(f"Profit: {profit_net:.2f} USD")

# Générer un lien pour les opportunités d'arbitrage
if arbitrage_opportunities:
    opportunities_text = "Arbitrage Opportunities:\n"
    for opportunity in arbitrage_opportunities:
        opportunities_text += (f"- {opportunity['crypto']} : Buy on {opportunity['buy_exchange']} at {opportunity['buy_price']} USD, "
                               f"Sell on {opportunity['sell_exchange']} at {opportunity['sell_price']} USD, "
                               f"Profit: {opportunity['profit']:.2f} USD\n")


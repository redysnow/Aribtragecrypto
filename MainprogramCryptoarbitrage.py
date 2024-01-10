#!/usr/bin/env python
# coding: utf-8

# # Main program arbitrage

# In[52]:


def find_largest_price_difference_percentage(prices):
    # Conversion des prix en nombres flottants et extraction des noms des plateformes
    platforms = list(prices.keys())
    values = [float(price) for price in prices.values()]

    # Trouver le prix le plus élevé et le plus bas
    max_price = max(values)
    min_price = min(values)

    # Trouver les plateformes correspondantes
    platform_max_price = platforms[values.index(max_price)]
    platform_min_price = platforms[values.index(min_price)]

    # Calcul de l'écart en pourcentage
    difference_percentage = ((max_price - min_price) / min_price) * 100

    return platform_max_price, platform_min_price, difference_percentage



# In[53]:


# Main program

# Importez d'abord toutes vos fonctions depuis le fichier APIpricecrypto.py
from APIpricecrypto import (get_binance_price, get_coinbase_price, 
                            get_kraken_price, get_bitfinex_price, 
                            get_huobi_price, get_gemini_price, 
                            get_kucoin_price, get_bitstamp_price, 
                            get_gateio_price, get_bitmex_price, 
                            get_exmo_price, get_cexio_price)

crypto_symbol = 'BTC'  # Symbol for Bitcoin

# Obtention des prix du Bitcoin sur différentes plateformes
binance_price = get_binance_price(crypto_symbol)
coinbase_price = get_coinbase_price(crypto_symbol)
#kraken_price = get_kraken_price(crypto_symbol)
bitfinex_price = get_bitfinex_price(crypto_symbol)
huobi_price = get_huobi_price(crypto_symbol)
gemini_price = get_gemini_price(crypto_symbol)
kucoin_price = get_kucoin_price(crypto_symbol)
bitstamp_price = get_bitstamp_price(crypto_symbol)
gateio_price = get_gateio_price(crypto_symbol)
#bitmex_price = get_bitmex_price(crypto_symbol)
exmo_price = get_exmo_price(crypto_symbol)
cexio_price = get_cexio_price(crypto_symbol)

# Affichage des prix obtenus
print("Binance:", binance_price)
print("Coinbase:", coinbase_price)
#print("Kraken:", kraken_price)
print("Bitfinex:", bitfinex_price)
print("Huobi:", huobi_price)
print("Gemini:", gemini_price)
print("KuCoin:", kucoin_price)
print("Bitstamp:", bitstamp_price)
print("Gate.io:", gateio_price)
#print("BitMEX:", bitmex_price)
print("EXMO:", exmo_price)
print("CEX.IO:", cexio_price)


# In[54]:


# Création d'un dictionnaire avec les prix obtenus
prices = {
    "Binance": binance_price,
    "Coinbase": coinbase_price,
    "Bitfinex": bitfinex_price,
    "Huobi": huobi_price,
    "Gemini": gemini_price,
    "KuCoin": kucoin_price,
    "Bitstamp": bitstamp_price,
    "Gate.io": gateio_price,
    "EXMO": exmo_price,
    "CEX.IO": cexio_price
}

# Utilisation de la fonction pour trouver le plus grand écart
platform_max, platform_min, diff= find_largest_price_difference(prices)
max_price = prices[platform_max]
min_price = prices[platform_min]
diff_percentage = (diff / float(min_price)) * 100
print(f"Le plus grand écart est entre {platform_max} ({max_price}) et {platform_min} ({min_price}) avec une différence de {diff_percentage} ({diff_percentage:.2f}%).")



# In[ ]:





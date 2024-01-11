#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Liste des cryptomonnaies
cryptos_symbols = [
    'BTC', 'ETH', 'XRP', 'XMR', 'LTC', 'BCH', 'EOS', 'XTZ', 'XLM', 'ADA',
    'LINK', 'DOT', 'YFI', 'UNI', 'AAVE', 'BSV', 'SOL', 'ATOM', 'BNB', 'TRX',
    'NEO', 'ALGO', 'ZEC', 'DOGE', 'DASH', 'VET', 'MKR', 'COMP', 'SNX', 'KSM',
    'AVAX', 'FIL', 'SUSHI', 'THETA', 'GRT', 'FTT', '1INCH', 'BAT', 'OMG', 'QTUM',
    'ZRX', 'CRV', 'LRC', 'SXP', 'BTT', 'ONT', 'NANO', 'ICX', 'ANKR', 'IOTA'
]


# In[2]:


# Seuil de différence de prix en pourcentage
seuil_diff = 0.05


# In[3]:


# Importez d'abord toutes vos fonctions depuis le fichier APIpricecrypto.py
from APIpricecrypto import (get_binance_price, get_coinbase_price, 
                            get_kraken_price, get_bitfinex_price, 
                            get_huobi_price, get_gemini_price, 
                            get_kucoin_price, get_bitstamp_price, 
                            get_gateio_price, get_bitmex_price, 
                            get_exmo_price, get_cexio_price)


# In[4]:


def find_largest_price_difference_percentage(prices):
    # Implémentez cette fonction pour trouver la plus grande différence de prix en pourcentage


    for crypto in cryptos_symbols:
        prices = {
    "Binance": get_binance_price(crypto),
    "Coinbase": get_coinbase_price(crypto),
    "Kraken": get_kraken_price(crypto),
    "Bitfinex": get_bitfinex_price(crypto),
    "Huobi": get_huobi_price(crypto),
    "Gemini": get_gemini_price(crypto),
    "KuCoin": get_kucoin_price(crypto),
    "Bitstamp": get_bitstamp_price(crypto),
    "Gate.io": get_gateio_price(crypto),
    "BitMEX": get_bitmex_price(crypto),
    "EXMO": get_exmo_price(crypto),
    "CEX.IO": get_cexio_price(crypto)
}


    # Filtrer les valeurs None
    valid_prices = {platform: price for platform, price in prices.items() if price is not None}

    if valid_prices:
        platform_max, platform_min, diff = find_largest_price_difference_percentage(valid_prices)
        if diff > seuil_diff:
            print(f"Écart important pour {crypto}: {platform_max} vs {platform_min} avec une différence de {diff}%")


# In[5]:


def generer_liens(platform, crypto_symbol):
   
    urls = {
        "Binance": f"https://www.binance.com/en/trade/{crypto_symbol}_USDT",
        "Coinbase": f"https://www.coinbase.com/price/{crypto_symbol.lower()}",
        "Kraken": f"https://www.kraken.com/prices/{crypto_symbol.lower()}-usd-price-chart",
        "Bitfinex": f"https://www.bitfinex.com/t/{crypto_symbol}:USD",
        "Huobi": f"https://www.huobi.com/en-us/exchange/{crypto_symbol.lower()}_usdt",
        "Gemini": f"https://www.gemini.com/prices/{crypto_symbol.lower()}",
        "KuCoin": f"https://www.kucoin.com/trade/{crypto_symbol}-USDT",
        "Bitstamp": f"https://www.bitstamp.net/markets/{crypto_symbol.lower()}/usd/",
        "Gate.io": f"https://www.gate.io/trade/{crypto_symbol}_USDT",
        "EXMO": f"https://exmo.com/en/trade/{crypto_symbol}_USD",
        "CEX.IO": f"https://cex.io/{crypto_symbol}-usd"
    }
    return urls.get(platform, f"https://example.com/{platform}/{crypto_symbol}")


# In[6]:


platforms = {
    "Binance": get_binance_price,
    "Coinbase": get_coinbase_price,
    "Kraken": get_kraken_price,
    "Bitfinex": get_bitfinex_price,
    "Huobi": get_huobi_price,
    "Gemini": get_gemini_price,
    "KuCoin": get_kucoin_price,
    "Bitstamp": get_bitstamp_price,
    "Gate.io": get_gateio_price,
    "BitMEX": get_bitmex_price,
    "EXMO": get_exmo_price,
    "CEX.IO": get_cexio_price
}


# In[7]:


from IPython.display import display, HTML


# # MAIN PROGRAM

# In[8]:


opportunities = None
opportunities = []  # Liste pour stocker les opportunités

for crypto_symbol in cryptos_symbols:
    print(f"\n====== Analyse des prix pour {crypto_symbol} ======")

    # Récupération et stockage des prix pour chaque plateforme
    prices = {platform: get_price(crypto_symbol) for platform, get_price in platforms.items()}

    # Affichage des prix obtenus pour chaque plateforme
    for platform, price in prices.items():
        print(f"{platform}: {price}")

    # Vérification si prices a des valeurs
    if prices.values():
        # Convertir chaque valeur en float avant de faire les calculs
        prices_float = {platform: float(price) for platform, price in prices.items() if price is not None}
        max_price_platform = max(prices_float, key=prices_float.get)
        min_price_platform = min(prices_float, key=prices_float.get)
        
        max_price = max(float(price) for price in prices.values() if price is not None)
        min_price = min(float(price) for price in prices.values() if price is not None)

        # Calcul de la différence en pourcentage
        diff = ((max_price - min_price) / min_price) * 100 if min_price > 0 else 0
    else:
        diff = 0
        
    if  diff > seuil_diff:
        buy_link = generer_liens(min_price_platform, crypto_symbol)
        sell_link = generer_liens(max_price_platform, crypto_symbol)
        buy_html = f"<a href='{buy_link}' target='_blank'>Acheter sur {min_price_platform} à {min_price} USD</a>"
        sell_html = f"<a href='{sell_link}' target='_blank'>Vendre sur {max_price_platform} à {max_price} USD</a>"
        spread_str = f"Différence en pourcentage: {diff:.2f}%"
        
        opportunity = {
            "Crypto": crypto_symbol,
            "Achat": buy_html,
            "Vente": sell_html,
            "Différence": spread_str,
        }
        
        opportunities.append(opportunity)
    else:
        print("Aucune donnée disponible pour le calcul.")


# In[9]:


# Afficher la synthèse des opportunités à la fin
print("\n===== Synthèse des Opportunités =====")
for opportunity in opportunities:
    display(HTML(f"Crypto: {opportunity['Crypto']}, {opportunity['Achat']}, {opportunity['Vente']}, {opportunity['Différence']}"))


# In[ ]:


# A revoir le spread  


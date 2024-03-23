from binance.client import Client

client = Client()

btc_usdt = client.get_symbol_ticker(symbol='BTCUSDT')
eth_usdt = client.get_symbol_ticker(symbol='ETHUSDT')
bnb_usdt = client.get_symbol_ticker(symbol='BNBUSDT')
print(btc_usdt,"USDT")
print(eth_usdt,"USDT")
print(bnb_usdt,"USDT")
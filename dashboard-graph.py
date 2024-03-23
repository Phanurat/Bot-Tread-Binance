import json
from binance.client import Client

client = Client()

btc_usdt = client.get_symbol_ticker(symbol='BTCUSDT')
eth_usdt = client.get_symbol_ticker(symbol='ETHUSDT')
bnb_usdt = client.get_symbol_ticker(symbol='BNBUSDT')
print(btc_usdt,"USDT")
print(eth_usdt,"USDT")
print(bnb_usdt,"USDT")

# สร้าง dictionary เก็บข้อมูล
data = {
    "BTCUSDT": btc_usdt,
    "ETHUSDT": eth_usdt,
    "BNBUSDT": bnb_usdt
}

# บันทึกข้อมูลในไฟล์ JSON
with open('json/prices.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("บันทึกข้อมูลเรียบร้อยแล้วในไฟล์ prices.json")
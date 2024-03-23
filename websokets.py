from binance.client import Client
from twisted.internet import reactor
from binance import AsyncClient, BinanceSocketManager

# สร้างการเชื่อมต่อกับ Binance API
client = Client()

# สร้าง WebSocket Manager
bm = BinanceSocketManager(client)

# สร้างฟังก์ชัน callback สำหรับการรับข้อมูลราคาแบบ Realtime
def process_message(msg):
    print("Symbol:", msg['s'], "ราคาล่าสุด:", msg['c'])

# สร้างการ subscribe ข้อมูลราคาแบบ Realtime สำหรับ BTC, ETH, และ BNB
btc_key = bm.start_symbol_ticker_socket(callback=process_message, symbol='BTCUSDT')
eth_key = bm.start_symbol_ticker_socket(callback=process_message, symbol='ETHUSDT')
bnb_key = bm.start_symbol_ticker_socket(callback=process_message, symbol='BNBUSDT')

# เริ่มการทำงานของ WebSocket Manager
bm.start()

# ให้โปรแกรมทำงานไปเรื่อยๆ จนกว่าจะมีการหยุดการทำงาน
reactor.run()

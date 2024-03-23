from binance.client import Client

# อ่าน API Key และ Secret Key จากไฟล์
def read_api_keys(file_path):
    with open(file_path, 'r') as file:
        api_keys = {}
        for line in file:
            key, value = line.strip().split('=')
            api_keys[key] = value
        return api_keys

# ระบุตำแหน่งของไฟล์ API Keys
api_keys_file = 'api_key.txt'

# อ่านคีย์จากไฟล์
api_keys = read_api_keys(api_keys_file)

# use key by reading key from file
api_key = api_keys['API_KEY']
api_secret = api_keys['API_SECRET']

# สร้างการเชื่อมต่อกับ Binance API
client = Client(api_key, api_secret)

# ดึงข้อมูลบัญชี
account_info = client.get_account()

# แสดงเฉพาะเหรียญที่มีจำนวนมากกว่าศูนย์ในบัญชี
ticker = client.get_symbol_ticker(symbol='BTCUSDT')
print(ticker,"USDT")
print("เหรียญที่มีในบัญชี:")
print("-----------------------")
for balance in account_info['balances']:
    if float(balance['free']) > 0 or float(balance['locked']) > 0:
        print(f"{balance['asset']}: จำนวนที่มี {balance['free']}, จำนวนที่ล็อก {balance['locked']}")

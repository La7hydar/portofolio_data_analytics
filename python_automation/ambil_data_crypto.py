import requests # Library untuk "minta" data ke internet

# Alamat API penyedia harga crypto
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=idr"

# 1. Kirim permintaan ke internet
respon = requests.get(url)

# 2. Ubah data mentah menjadi format yang bisa dibaca Python (JSON)
data = respon.json()

# 3. Ambil harga spesifiknya
harga_btc = data['bitcoin']['idr']

print(f"Harga Bitcoin saat ini adalah: Rp {harga_btc:,}")

# Coba ambil harga dalam USD juga
url_lengkap = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=idr,usd"
data_baru = requests.get(url_lengkap).json()

print(f"Harga USD: {data_baru['bitcoin']['usd']}")
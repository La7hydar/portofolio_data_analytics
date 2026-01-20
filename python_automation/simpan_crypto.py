import requests
import pandas as pd 
from datetime import datetime 
# 1. Ambil data
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=idr"
respon = requests.get(url).json()

# 2. Siapkan data untuk jadi tabel
harga = respon['bitcoin']['idr']
waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 3. Masukkan ke format tabel (Dictionary)
data_untuk_tabel = {
    'waktu_cek': [waktu],
    'nama_koin': ['Bitcoin'],
    'harga_idr': [harga]
}

# 4. Ubah jadi DataFrame (Tabel ala Excel di Python)
df = pd.DataFrame(data_untuk_tabel)

# 5. Simpan ke file CSV (mode='a' artinya Append/Menumpuk)
# Jika file belum ada, dia buat baru. Jika sudah ada, dia nambah di bawahnya.
df.to_csv('data_harga_crypto.csv', mode='a', index=False, header=not pd.io.common.file_exists('data_harga_crypto.csv'))

print("Data berhasil disimpan ke CSV!") 
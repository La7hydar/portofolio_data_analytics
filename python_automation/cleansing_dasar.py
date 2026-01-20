import pandas as pd
import numpy as np # Library untuk menangani data kosong

# 1. Simulasi data kotor (Contoh: ada harga 0 dan data kosong)
data_kotor = {
    'produk': ['Bitcoin', 'Ethereum', 'Dogecoin', 'Cardano'],
    'harga': [1500000000, None, 0, 15000]
}

df = pd.DataFrame(data_kotor)

# 2. PROSES CLEANSING
# A. Hapus baris yang harganya kosong (None/NaN)
df_clean = df.dropna(subset=['harga'])

# B. Ganti harga yang 0 menjadi rata-rata (atau hapus juga boleh)
# Di sini kita pilih untuk hapus saja yang harganya <= 0
df_clean = df_clean[df_clean['harga'] > 0]

print("Data Sebelum Cleansing:")
print(df)
print("\nData Setelah Cleansing (Hanya yang valid):")
print(df_clean)
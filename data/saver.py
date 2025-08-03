import pandas as pd
from datetime import datetime

def save (input, result):
    data = {
        "Waktu": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "Input": [input],
        "Hasil": [result]
    }

    df = pd.DataFrame(data)

    filename = "hasil_pencarian_kambing.xlsx"

    try:
        # Jika file sudah ada, tambahkan ke data lama
        existing_df = pd.read_excel(filename)
        combined_df = pd.concat([existing_df, df], ignore_index=True)
    except FileNotFoundError:
        # Jika belum ada, pakai df baru
        combined_df = df

    # Simpan ke file
    combined_df.to_excel(filename, index=False)
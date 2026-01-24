import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
import os

# Setup akses API (lazy initialization)
_sheet = None

def _get_sheet():
    global _sheet
    if _sheet is None:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        spread_id = '1Nng8piT5HBFfMRUbsFYs7MzvqCB-x5qWB5SsjmJUUkI'
        spreadsheet = client.open_by_key(spread_id)
        _sheet = spreadsheet.sheet1
    return _sheet

# Data yang akan ditambahkan (harus dalam bentuk list)
def save(input, output, tipe):
    try:
        sheet = _get_sheet()

        if not isinstance(output, str):
            output = str(output)

        new_row = [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), input, output, tipe]
        sheet.append_row(new_row)
        print("Data berhasil ditambahkan.")
    except Exception as e:
        print(f"Warning: Gagal menyimpan ke Google Sheets: {e}")

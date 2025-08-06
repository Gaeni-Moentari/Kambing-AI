import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials

# Setup akses API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

# Buka spreadsheet dan worksheet
spread_id = '1Nng8piT5HBFfMRUbsFYs7MzvqCB-x5qWB5SsjmJUUkI'
spreadsheet = client.open_by_key(spread_id)
sheet = spreadsheet.sheet1  # atau spreadsheet.worksheet('NamaSheet')

# Data yang akan ditambahkan (harus dalam bentuk list)
def save(input, output, tipe):
    
    if not isinstance(output, str):
        output = str(output)
        
    new_row = [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), output, output, tipe]
    sheet.append_row(new_row)
    print("Data berhasil ditambahkan.")

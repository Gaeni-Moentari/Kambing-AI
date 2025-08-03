import base64
import streamlit as st

# Fungsi untuk mendapatkan base64 dari file biner
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as file:
        binary_data = file.read()
        base64_data = base64.b64encode(binary_data).decode('utf-8')
    return base64_data

# Fungsi untuk menampilkan gambar dengan penyesuaian jumlah card
def image(file_paths):
    style_block = f"""
        <style>
        .LogoContainer {{
            display: flex;
            align-items: center;
            justify-content: center; /* Tetap rata tengah */
            flex-wrap: wrap; /* Membungkus jika tidak muat */
            gap: 15px; /* Jarak antar logo */
            padding: 10px;
            background: #fff;
            margin: 0 auto;
            width: 100%; /* Container fleksibel sesuai layar */
            box-sizing: border-box; /* Hindari overflow */
        }}
        .Logo {{
            height: auto; /* Tinggi proporsional */
            width: 100px;
            max-width: 100px; /* Lebar maksimal logo */
            object-fit: contain;
            margin: 5px; /* Jarak antar logo */
        }}
        @media (max-width: 768px) {{
            .LogoContainer{{
                display: inline-block;
            }}
            .Logo {{
                width: 60px; /* Logo lebih kecil di layar mobile */
            }}
        }}
        </style>
    <div class="LogoContainer">
    """
    
    # Menambahkan setiap gambar
    for file_path in file_paths:
        image_base64 = get_base64_of_bin_file(file_path)
        style_block += f"""<img src="data:image/png;base64,{image_base64}" class="Logo">"""
    
    style_block += "</div>"
    
    # Render di Streamlit
    st.markdown(style_block, unsafe_allow_html=True)
    

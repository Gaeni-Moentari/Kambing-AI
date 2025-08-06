import streamlit as st
import pandas as pd


st.title("Data Produk")

# Contoh Data
data = {
    "ID": [1, 2],
    "Nama Produk": ["Sabun", "Shampoo"],
    "Harga": [5000, 10000]
}

df = pd.DataFrame(data)
st.dataframe(df)
import streamlit as st
import pandas as pd

st.title("Data Kategori")

# Contoh Data
data = {
    "ID Kategori": [101, 102],
    "Nama Kategori": ["Perawatan", "Kebersihan"]
}

df = pd.DataFrame(data)
st.dataframe(df)

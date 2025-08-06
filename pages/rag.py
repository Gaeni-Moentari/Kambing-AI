from AI_Component.Crew import *
import Component.Logo as Img
from sheets import save
import streamlit as st

st.set_page_config(page_title="Aplikasi Multi-Halaman", layout="wide")

Img.image(["./Image/gema.png"])
st.title("AI Kambing GEMA dengan RAG")
st.write("Model yang menggunakan RAG versi kedua dari GEMA menggunakan data data dari Aplikasi kambingku www.kambingku.com")
st.write("Koordinator Gatot HP - www.gaeni.org ")
input = st.text_input("Masukkan pertanyaan ")
lang = "bahasa indonesia"
submit = st.button("Mulai Pencarian")

if submit:
    result = KokoaCrew(input, lang).ragCrew().kickoff()
    st.markdown(result)
    save(input, result, 'RAG')
    

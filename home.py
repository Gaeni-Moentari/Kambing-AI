from AI_Component.Crew import *
import Component.Logo as Img
from sheets import save
import streamlit as st

st.set_page_config(page_title="AI Kambing GEMA", layout="wide")

Img.image(["./Image/gema.png"])
st.title("AI Kambing GEMA")
st.write("Model awal pengembangan Model Trained AI Kambing GEMA. Program ini diharapkan bisa dimanfaatkan oleh siswa/mahasiswa/masyarakat yang ingin mendapatkan referensi untuk produksi di daerahnya.")
st.write("Koordinator Gatot HP - www.gaeni.org ")
input = st.text_input("Masukkan pertanyaan ")
lang = "bahasa indonesia"
submit = st.button("Mulai Pencarian")

if submit:
    result = KokoaCrew(input, lang).generalCrew().kickoff()
    st.markdown(result)
    save(input, result, 'Tavily')
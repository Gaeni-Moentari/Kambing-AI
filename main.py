from AI_Component.Crew import *
import Component.Logo as Img
from sheets import save
import streamlit as st

st.set_page_config(page_title="AI Kambing GEMA", layout="wide")

Img.image(["./Image/gema.png"])
st.title("AI Kambing GEMA")
st.write("Model awal pengembangan Model Trained AI Kambing GEMA. Program ini diharapkan bisa dimanfaatkan oleh siswa/mahasiswa/masyarakat yang ingin mendapatkan referensi untuk produksi di daerahnya.")
st.write("Koordinator Gatot HP - www.gaeni.org ")

# Tambahan: Contoh pertanyaan untuk memulai
st.subheader("Mari mulai dengan beberapa pertanyaan seperti:")
example_questions = [
    "Bagaimana beternak kambing",
    "Bagaimana Pengolahan Pakan Kambing", 
    "Bagaimana pengolahan kambing"
]

# Menampilkan contoh pertanyaan sebagai buttons yang bisa diklik
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🐐 " + example_questions[0]):
        st.session_state.selected_question = example_questions[0]
        
with col2:
    if st.button("🌾 " + example_questions[1]):
        st.session_state.selected_question = example_questions[1]
        
with col3:
    if st.button("🥩 " + example_questions[2]):
        st.session_state.selected_question = example_questions[2]

# Input field dengan nilai default dari pertanyaan yang dipilih
default_value = st.session_state.get('selected_question', '')
input = st.text_input("Masukkan pertanyaan ", value=default_value)

lang = "bahasa indonesia"

# Initialize session state
if 'is_loading' not in st.session_state:
    st.session_state.is_loading = False
if 'result' not in st.session_state:
    st.session_state.result = None
if 'last_question' not in st.session_state:
    st.session_state.last_question = None

# Submit button with loading state
submit = st.button("🔄 Sedang Memproses..." if st.session_state.is_loading else "Mulai Pencarian", 
                   disabled=st.session_state.is_loading)

if submit and input.strip():
    # Set loading state to True and clear previous result
    st.session_state.is_loading = True
    st.session_state.result = None
    st.session_state.last_question = input
    
    # Process immediately without rerun
    with st.spinner('Sedang mencari informasi...'):
        try:
            result = KokoaCrew(input, lang).generalCrew().kickoff()
            st.session_state.result = result
            st.session_state.last_question = input
            save(input, result, 'Tavily')
        except Exception as e:
            st.session_state.result = f"❌ **Terjadi kesalahan:** {str(e)}"
        finally:
            # Reset loading state
            st.session_state.is_loading = False

# Display result if available
if st.session_state.result is not None:
    st.divider()
    st.subheader(f"Hasil untuk: {st.session_state.last_question}")
    st.markdown(st.session_state.result)
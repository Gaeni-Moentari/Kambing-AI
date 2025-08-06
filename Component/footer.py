import streamlit as st

footer = """
<style>
footer {
    visibility: hidden;
}
.footer-custom {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #f0f2f6;
    color: #000;
    text-align: center;
    padding: 10px;
    font-size: 14px;
}
</style>

<div class="footer-custom">
    Dikembangkan oleh GEMA · © 2025
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
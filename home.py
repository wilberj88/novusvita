import streamlit as st
import pandas as pd
import numpy as np

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Vita", page_icon="♥")

st.title('Novus Vita ♥')

st.header("Define tu esencia ✍️")
st.subheader("Enfócate en ella 🎯")
st.subheader("Construye una Nueva Vida♥")

with st.form(key='my_form'):
   username = st.text_input('Username')
   password = st.text_input('Password')
   st.form_submit_button('Login')

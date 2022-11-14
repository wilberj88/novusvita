#IMPORTAMOS LIBRERÍAS
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
import altair as alt
import pydeck as pdk
import matplotlib.pyplot as plt
import datetime
import base64

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Vita", page_icon="♥")
st.title('Novus Vita ♥')
st.header("Define tu esencia ✍️")
st.subheader("Enfócate en ella 🎯")
st.subheader("Construye una Nueva Vida♥")

#SUBTITULO
st.write('---')
st.write("""
**Cuatro (4) Centrales de Mando para tu IKIGAI:**
- ♥: `Pasión: ¿Qué amas?`
- 🧠: `Vocación: ¿En qué eres bueno?`
- 🌎: `Misión: ¿Cómo aportas al planeta?`
- 💰: `Profesión: ¿En qué deseas ganar dinero?`
""")
st.write("""
**Sistema de Alarmas para:**
- ⏰ : `Retrasos en Cumplimientos de Metas`
""")
st.write("""
**Sistema de Recomendación para:**
- 📈:  `Mayores resultados`
""")
st.write('---')


st.write('Pasión ♥')
st.multiselect('Selecciona tus principales pasatiempos', ['Leer', 'Ejercicio', 'Cine'])
st.text_input('Indica cómo sería tu vida ideal')
option = st.selectbox(
    'Indícanos 3 materias preferidas del colegio',
    ('Matemáticas', 'Filosofía', 'Física', 'Biología', 'Deportes'))


st.write('Vocación 🧠')
st.text_input('Indícanos actualmente en qué te ganas la vida')
st.text_input('Indícanos en cuáles disciplinas te consideres más competente')


st.write('Misión 🌎')
st.multiselect('Selecciona los problemas del planeta que deseas enfrentar', ['Hambre', 'Pobreza', 'Educacion'])

st.write('Profesión 💰')
st.selectbox('Elige el rol más demandado a futuro que desees abordar', ['Data Scientist', 'Broker', 'ML Operator'])






#MONITOR 1: VITA
st.header("Monitor 📺 de Vita  ♥ + 🧠 + 🌎 + 💰")
col1, col2, col3, col4 = st.columns(4)
col1.metric(label ="Pasión", value = '85%', delta='17')
col2.metric("Vocación", "195%", "13")
col3.metric("Misión", "87%", "7")
col4.metric("Profesión", "87%", "7")

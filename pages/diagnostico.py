import streamlit as st


st.title('Define tu esencia')

st.selectbox('Elige el rol más demandado a futuro que desees abordar', ['Data Scientist', 'Broker', 'ML Operator'])
st.multiselect('Elige los problemas del planeta que deseas enfrentar', ['Hambre', 'Pobreza', 'Educacion'])

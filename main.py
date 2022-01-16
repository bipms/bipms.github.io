import streamlit as st
import pandas as pd


st.sidebar.write("**Silahkan pilih nama UMKM/Klaster Anda**")
st.sidebar.selectbox('Nama UMKM/Klaster',[1,2,3])
st.sidebar.button('Pilih')


option = st.sidebar.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))
st.sidebar.write('Produk yang dicatat di SIKEPANG:')

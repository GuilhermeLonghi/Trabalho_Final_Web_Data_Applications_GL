import streamlit as st
import pandas  as pd
import plotly.express as px

st.write('**Pesquisa Universidades**')
st.sidebar.header('Pesquise a universidades')

df = pd.read_csv('../1_bases_tratadas/dados_tratados.csv', sep=';', encoding='utf-8')

uni = df['Nome da Instituição']
escolha_uni = st.sidebar.selectbox('Escolha a universidade', uni)

uni2 = df['País']
escolha_uni = st.sidebar.selectbox('Escolha o país', uni2)

uni3 = df['Pontos']
escolha_uni = st.sidebar.selectbox('Escolha a pontuação', uni3)

df2 = df[df['Nome da Instituição']==escolha_uni]

fig = px.bar(df2, x='Nome da Instituição', y='Pontos')
st.bar_chart(fig)


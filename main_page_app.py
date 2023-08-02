import streamlit as st
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)

def main_page(df):
    st.title("Página Inicial")
    st.write("Bem-vindo ao projeto de Expectativa de Vida!")
    st.write("A base de dados abrange o período de 2000 a 2015 e contém informações de 193 países.")

    
    st.header("Informações da base de dados")
    st.write(f"Número de amostras: {df.shape[0]}")
    st.write(f"Número de colunas: {df.shape[1]}")
    st.write(f"Colunas disponíveis: {', '.join(df.columns)}")

    
    st.header("Amostra dos Dados")
    st.write("Aqui estão os primeiros registros da base de dados:")
    st.dataframe(df.head())

    
    st.header("Estatísticas Descritivas")
    st.write("Aqui estão algumas estatísticas descritivas para as colunas numéricas:")
    st.write(df.describe())


    st.write("")
    st.info("Para navegar, utilize o menu na barra lateral à esquerda.")
    st.write("")

    st.markdown("Desenvolvido por Rafaella Moura e Taciana Vasconcelos") 

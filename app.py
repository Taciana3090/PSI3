import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import altair as alt
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Configuração para remover o aviso "PyplotGlobalUseWarning"
st.set_option('deprecation.showPyplotGlobalUse', False)

# Definindo as configurações da página
st.set_page_config(
    page_title="Projeto III - Expectativa de Vida",
    page_icon='📊',
    layout="wide",
    initial_sidebar_state="auto"
)

# URL do arquivo
file_url = "https://github.com/Taciana3090/PSI3/raw/Taciana3090/master/data/Life%20Expectancy%20Data.csv"

# Carregar o conjunto de dados
df = pd.read_csv(file_url)

# Título e descrição
st.write("# Dashboard Expectativa de Vida")
st.markdown("Este dashboard tem como objetivo apresentar uma análise interativa da expectativa de vida em diferentes países.")
st.markdown("O conjunto de dados abrange o período de 2000 a 2015 e contém informações de 193 países.")

# Páginas
def data_page():
    st.subheader("Visão Geral dos Dados")
    
    # Exibir a quantidade de linhas e colunas
    st.write(f"Total de linhas: {df.shape[0]}")
    st.write(f"Total de colunas: {df.shape[1]}")
    
    # Exibir as primeiras linhas do DataFrame
    st.subheader("Amostra dos Dados")
    st.write(df.head())
    
    # Contagem dos valores ausentes
    st.subheader("Contagem de Valores Ausentes")
    st.write(df.isnull().sum())
    
    # Estatísticas descritivas das colunas numéricas
    st.subheader("Estatísticas Descritivas (Colunas Numéricas)")
    st.write(df.describe())

# Sidebar com botões
pages = {
    "Análise Exploratória Inicial": data_page
   
}

# Renderizar a página selecionada
selection = st.sidebar.radio("Selecione uma Página", list(pages.keys()))
pages[selection]()

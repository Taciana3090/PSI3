import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import altair as alt
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

#  remove o aviso "PyplotGlobalUseWarning"
st.set_option('deprecation.showPyplotGlobalUse', False)

# definindo as configurações da página
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

def filters_page():
    st.subheader("Filtros")
    selected_country = st.sidebar.selectbox('Selecione um país', df['Country'].unique())
    selected_year = st.sidebar.selectbox('Selecione um ano', df['Year'].unique())
    selected_status = st.sidebar.selectbox('Selecione o status', df['Status'].unique())

    # aplicando o filtro de country, ano e status
    filtered_df = df[(df['Country'] == selected_country) & (df['Year'] == selected_year) & (df['Status'] == selected_status)]

    # exibindo resultado
    st.subheader("Resultado")
    if filtered_df.empty:
        st.warning("Nenhum resultado encontrado com os filtros selecionados.")
    else:
        st.dataframe(filtered_df)

def charts_page():
    
    # selecionando o país, status e variável
    selected_country = st.sidebar.selectbox('Selecione um país', df['Country'].unique())
    selected_status = st.sidebar.selectbox('Selecione o status', df['Status'].unique())
    selected_variable = st.sidebar.selectbox('Selecione uma variável', df.select_dtypes(include='number').columns)
    
    # filtrando o com base nos filtros selecionados
    filtered_df = df[(df['Country'] == selected_country) & (df['Status'] == selected_status)]
    if filtered_df.empty:
        st.warning("Nenhum resultado encontrado com os filtros selecionados.")
    else:
        # gráfico de Linhas para a variável selecionada ao longo do tempo
        st.subheader(f"{selected_variable} ao longo do tempo")
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=filtered_df['Year'], y=filtered_df[selected_variable], mode='lines+markers', name=selected_variable))
        z = np.polyfit(filtered_df['Year'], filtered_df[selected_variable], 1)
        p = np.poly1d(z)
        fig.add_trace(go.Scatter(x=filtered_df['Year'], y=p(filtered_df['Year']), mode='lines', name='Tendência'))
        fig.update_layout(showlegend=True)
        st.plotly_chart(fig)

    

# Sidebar com botões
pages = {
    "Análise Exploratória Inicial": data_page,
    "Filtros": filters_page,
    "Gráficos": charts_page
   
}

# Renderizar a página selecionada
selection = st.sidebar.radio("Selecione uma Página", list(pages.keys()))
pages[selection]()

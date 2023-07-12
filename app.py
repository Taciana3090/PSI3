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
        

 # Função para a página de Informações
def info_page():
    st.subheader("Informações")
     

    # Adicionar mais informações
    
    st.write("<div style='border: 3px solid black; padding: 10px; background-color: #2F4F4F; font-weight: bold;'>Especificações sobre os atributos</div>", unsafe_allow_html=True)

    st.write("<div style='border: 3px solid black; padding: 10px;'> </div>", unsafe_allow_html=True)
   
   
    st.write("<div style='border: 1px solid black; padding: 10px;'>country: O nome do país.</div>", unsafe_allow_html=True)
    st.write("<div style='border: 1px solid black; padding: 10px;'>year: O ano correspondente aos dados.</div>", unsafe_allow_html=True)
    st.write("<div style='border: 1px solid black; padding: 10px;'>status: O status de desenvolvimento do país (por exemplo, desenvolvido ou em desenvolvimento).</div>", unsafe_allow_html=True)
    st.write("<div style='border: 1px solid black; padding: 10px;'>life_expectancy: A expectativa de vida média em anos.</div>", unsafe_allow_html=True)
    st.write("<div style='border: 1px solid black; padding: 10px;'>adult_mortality: A taxa de mortalidade de adultos por 1.000 pessoas.</div>", unsafe_allow_html=True)
    st.write("<div style='border: 1px solid black; padding: 10px;'>infant_deaths: O número de mortes de crianças com menos de 1 ano.</div>", unsafe_allow_html=True)
    st.write("<div style='border: 1px solid black; padding: 10px;'>alcohol: O consumo de álcool por litro de álcool puro.</div>", unsafe_allow_html=True)
    st.write("<div style='border: 1px solid black; padding: 10px;'>percentage_expenditure: A despesa com saúde como uma porcentagem do Produto Interno Bruto (PIB) per capita.</div>", unsafe_allow_html=True)
    st.write("<div style='border: 1px solid black; padding: 10px;'>hepatitis_b: A cobertura vacinal contra hepatite B em crianças de 1 ano.</div>", unsafe_allow_html=True)
    st.write("<div style='border: 1px solid black; padding: 10px;'>measles: O número de casos de sarampo reportados.</div>", unsafe_allow_html=True)
    st.write("<div style='border: 1px solid black; padding: 10px;'>bmi: O índice de massa corporal médio da população.</div>", unsafe_allow_html=True)
    st.write("<div style='border: 1px solid black; padding: 10px;'>under-five_deaths: O número de mortes de crianças menores de 5 anos.</div>", unsafe_allow_html=True)
    st.write("<div style='border: 1px solid black; padding: 10px;'>polio: A cobertura vacinal contra poliomielite em crianças de 1 ano.</div>", unsafe_allow_html=True)
    st.write("<div style='border: 1px solid black; padding: 10px;'>total_expenditure: A despesa total com saúde como uma porcentagem do PIB.</div>", unsafe_allow_html=True)    
    st.write("<div style='border: 1px solid black; padding: 10px;'>diphtheria: A cobertura vacinal contra difteria em crianças de 1 ano.</div>", unsafe_allow_html=True)
    st.write("<div style='border: 1px solid black; padding: 10px;'>hiv/aids: A prevalência de HIV/AIDS por 1.000 pessoas.</div>", unsafe_allow_html=True)
    st.write("<div style='border: 1px solid black; padding: 10px;'>gdp: O Produto Interno Bruto per capita.</div>", unsafe_allow_html=True)
    st.write("<div style='border: 1px solid black; padding: 10px;'>population: A população total.</div>", unsafe_allow_html=True)
    st.write("<div style='border: 1px solid black; padding: 10px;'>thinness_1-19_years: A prevalência de desnutrição em pessoas de 1 a 19 anos.</div>", unsafe_allow_html=True)
    st.write("<div style='border: 1px solid black; padding: 10px;'>thinness_1-19_years: A prevalência de desnutrição em pessoas de 1 a 19 anos.</div>", unsafe_allow_html=True)
    st.write("<div style='border: 1px solid black; padding: 10px;'>thinness_5-9_years: A prevalência de desnutrição em crianças de 5 a 9 anos.</div>", unsafe_allow_html=True)
    st.write("<div style='border: 1px solid black; padding: 10px;'>income_composition_of_resources: O índice de composição de recursos (indicador do desenvolvimento humano).</div>", unsafe_allow_html=True)
    st.write("<div style='border: 1px solid black; padding: 10px;'>schooling: A média de anos de escolaridade.</div>", unsafe_allow_html=True)

    

    # Adicionar um link
    st.markdown("[Saiba mais sobre a fonte dos dados](https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who)")   

# Sidebar com botões
pages = {
    "Análise Exploratória Inicial": data_page,
    "Filtros": filters_page,
    "Gráficos": charts_page,
    "Informações": info_page
   
}

# Renderizar a página selecionada
selection = st.sidebar.radio("Selecione uma Página", list(pages.keys()))
pages[selection]()

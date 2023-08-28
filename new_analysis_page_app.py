import streamlit as st
import pandas as pd
import plotly.express as px


def new_analysis_page(df):
    st.title("Nova Análise Exploratória")
    st.write("Nesta página, você pode realizar uma análise exploratória adicional sobre a base de dados.")

    color_discrete_map = {'Desenvolvido': 'blue', 'Em Desenvolvimento': 'lightblue'}
    df['status'] = df['status'].replace({'Developing': 'Em Desenvolvimento', 'Developed': 'Desenvolvido'})

    # Contagem de países únicos por status
    status_counts = df.drop_duplicates(subset=['country']).groupby('status').size().reset_index(name='Número de Países')

    # Gráfico 1: Distribuição por Status Socioeconômico
    fig = px.bar(status_counts, x='status', y='Número de Países', color='status', title='Distribuição por Status Socioeconômico')
    st.plotly_chart(fig)

    # média de consumo de álcool entre países desenvolvidos e em desenvolvimento - gráfico 3
    avg_alcohol_by_status = df.groupby('status')['alcohol'].mean().reset_index()
    fig_bar = px.bar(avg_alcohol_by_status, 
                     x='status', 
                     y='alcohol', 
                     color='status', 
                     title='Comparação da Média de Consumo de Álcool entre Países Desenvolvidos e em Desenvolvimento',
                     color_discrete_map=color_discrete_map)
    st.plotly_chart(fig_bar)

    # 10 primeiros países com maior consumo de álcool nos países desenvolvidos - gráfico 4
    developed_countries = df[df['status'] == 'Desenvolvido']
    avg_alcohol_by_country = developed_countries.groupby('country')['alcohol'].mean().reset_index()
    avg_alcohol_by_country = avg_alcohol_by_country.sort_values(by='alcohol', ascending=True) 
    top_10_countries = avg_alcohol_by_country.tail(10)  
    fig_bar = px.bar(top_10_countries, 
                     x='alcohol', 
                     y='country', 
                     orientation='h', 
                     title='10 Países Desenvolvidos com Maior Consumo Médio de Álcool',
                     labels={'alcohol': 'Consumo Médio de Álcool', 'country': 'País'})
    st.plotly_chart(fig_bar)

    # média Mortalidade Infantil e Adulta  - gráfico 5
    df_mortality = df[['status', 'infant_deaths', 'adult_mortality']]
    avg_mortality = df_mortality.groupby('status').mean().reset_index()
    fig_mortality = px.bar(avg_mortality, 
                            x='status', 
                            y=['infant_deaths', 'adult_mortality'], 
                            title='Comparação de Mortalidade Infantil e Mortalidade Adulta por Status de Desenvolvimento',
                            barmode='group',
                            color_discrete_map={'infant_deaths': 'blue', 'adult_mortality': 'lightblue'})
    fig_mortality.update_traces(legendgroup='status')
    fig_mortality.update_layout(legend_title_text='Tipo de Mortalidade')
    st.plotly_chart(fig_mortality)


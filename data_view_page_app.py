import streamlit as st
import pandas as pd
import plotly.express as px

def data_view_page(df):
    st.title("Visualização dos Dados")
    st.write("Nesta página, você pode visualizar os dados do conjunto de dados.")

    # gráfico de barras 
    df_status_mean = df.groupby('status')['life_expectancy'].mean().reset_index()
    fig_bar = px.bar(df_status_mean, x='status', y='life_expectancy', 
                     title='Comparação da Expectativa de Vida média entre diferentes status de países',
                     labels={'status': 'Status do País', 'life_expectancy': 'Expectativa de Vida Média'},
                     template='plotly_dark')
    st.plotly_chart(fig_bar)


    # filtrando os dados pelo status e país
    status_options = df['status'].unique()
    selected_status = st.selectbox("Filtrar por status do País:", status_options)
    df_filtered = df[df['status'] == selected_status]
    country_options = df_filtered['country'].unique()
    selected_country = st.selectbox("Selecione um país:", country_options)
    df_filtered = df_filtered[df_filtered['country'] == selected_country]

    # gráfico de linha interativo com plotly Express 
    fig_line = px.line(df_filtered.sort_values(by='year'), x='year', y='life_expectancy', 
                  title=f'Expectativa de Vida em {selected_country} ao longo dos anos',
                  labels={'year': 'Ano', 'life_expectancy': 'Expectativa de Vida'},
                  template='plotly_dark', markers=True)
    st.plotly_chart(fig_line)

    # gráfico de dispersão 
    fig_scatter = px.scatter(df_filtered, x='gdp', y='life_expectancy', 
                             title=f'Relação entre Expectativa de Vida e PIB (GDP) em {selected_country}',
                             labels={'gdp': 'PIB (GDP)', 'life_expectancy': 'Expectativa de Vida'},
                             template='plotly_dark', color='year', size='population', hover_name='year')
    st.plotly_chart(fig_scatter)

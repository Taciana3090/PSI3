import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def statistical_analysis_page(df):
    st.title("Análise Exploratória")
    st.write("Nesta página, você pode realizar análises estatísticas sobre o conjunto de dados.")

    # análise sobre dados ausentes
    st.header("Dados Ausentes")
    null_df = get_null_data(df)
    st.dataframe(null_df)
def get_null_data(df):
    a = list(df.columns)
    b = []
    for i in a:
        c = df[i].isnull().sum()
        b.append(c)
    null_df = pd.DataFrame({'Nome da coluna': a, 'N° de valores ausentes': b})
    null_df['Porcentagem ausente (%)'] = round((null_df['N° de valores ausentes'] / len(df)) * 100, 2)
    null_df = null_df.sort_values('N° de valores ausentes')
    null_df['Porcentagem ausente (%)'] = null_df['Porcentagem ausente (%)'].astype(str) + '%'
    return null_df

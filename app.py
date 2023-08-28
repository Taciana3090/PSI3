import streamlit as st
import pandas as pd
from main_page_app import main_page
from data_view_page_app import data_view_page
from statistical_analysis_page_app import statistical_analysis_page
from new_analysis_page_app import new_analysis_page
from regression_models_page_app import regression_models_page


file_url = "https://github.com/Taciana3090/PSI3/raw/Taciana3090/master/data/Life%20Expectancy%20Data.csv"
df = pd.read_csv(file_url)

# padroniza o nome das colunas
orig_cols = list(df.columns)
new_cols = []
for col in orig_cols:
    new_cols.append(col.strip().replace('  ', ' ').replace(' ', '_').lower())

df.columns = new_cols
# renomeia a coluna 'thinness_1-19_years' para 'thinness_10-19_years'
df.rename(columns={'thinness_1-19_years': 'thinness_10-19_years'}, inplace=True)

# donfiguração da página 
st.set_page_config(
    page_title="Expectativa de vida 🌎",
    layout="wide",
)

def main():
    st.sidebar.empty()
    st.sidebar.title("Menu")
    page = st.sidebar.radio("Navegue para:", 
                            ["Página Inicial", "Visualização dos Dados", "Análise Exploratória", "Análise Exploratória II", "Modelos de Regressão"])

    # seleciona a página do menu
    if page == "Página Inicial":
        main_page(df)  
    elif page == "Visualização dos Dados":
        data_view_page(df)  
    elif page == 'Análise Exploratória':
        statistical_analysis_page(df)   
    elif page == 'Análise Exploratória II':
        new_analysis_page(df)
    elif page == "Modelos de Regressão":
        regression_models_page()


if __name__ == "__main__":
    main()

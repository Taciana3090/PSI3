import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def statistical_analysis_page(df):
    st.title("Análise Exploratória")
    st.write("Nesta página, você pode obter análises estatísticas sobre a base de dados.")

    # dados ausentes
    st.header("Dados Ausentes")
    null_df = get_null_data(df)
    st.dataframe(null_df)
    
    # Selecionar apenas as colunas numéricas (exceto 'life_expectancy')
    df_numeric = df.select_dtypes(include=[np.number])
    df_numeric = df_numeric.drop(columns=['life_expectancy'], errors='ignore')
    st.header("Correlações com 'life_expectancy'")
    correlation_matrix = df_numeric.corrwith(df['life_expectancy']).sort_values(ascending=False)

    # tabela de correlações
    st.dataframe(correlation_matrix)

    # resumo das correlações
    st.subheader("Resumo das Correlações")
    st.write("Ao analisar as correlações com a expectativa de vida ('life_expectancy'), podemos destacar as seguintes relações:")
    st.write("- Forte Influência Positiva: Fatores relacionados à educação, como 'schooling', e ao desenvolvimento econômico, como 'income_composition_of_resources', apresentam correlações positivas significativas. Além disso, a 'bmi' (Índice de Massa Corporal) e cobertura de vacinas como 'diphtheria' e 'polio' também estão positivamente correlacionadas com a expectativa de vida.")
    st.write("- Forte Influência Negativa: Questões de saúde como 'hiv/aids' e 'adult_mortality' apresentam correlações negativas significativas, indicando que o aumento dessas variáveis está associado a uma redução na expectativa de vida.")
    st.write("- Pouca Influência: Algumas variáveis, como 'population', 'measles' e 'infant_deaths', mostraram correlações próximas a zero, sugerindo que esses fatores não têm uma influência linear significativa na expectativa de vida.")
    
    # resumo da assimetria e da curtose
    st.header("Assimetria e Curtose")
    st.dataframe(get_skew_kurtosis(df_numeric))
    st.write("A assimetria mede o grau de desvio de uma distribuição em relação à distribuição normal.")
    st.write("A curtose mede a forma da distribuição, em relação a uma distribuição normal.")

    # resumo das distribuições
    st.subheader("Resumo das Distribuições")
    st.write("As distribuições dos dados podem ser classificadas em três tipos principais:")

    st.markdown("1. **Distribuição Normal:** Forma semelhante a um sino, com valores bem distribuídos em torno da média. "
                "Geralmente, não apresenta muitos valores extremos (outliers).")

    st.markdown("2. **Distribuição Não-Normal:** Dados assimétricos, podendo ter valores concentrados em uma cauda da curva. "
                "Podem conter valores extremos (outliers).")

    st.markdown("3. **Distribuição Platicúrtica:** Dados mais concentrados e menos propensos a apresentar valores extremos (outliers).")    
    
    normal_cols = ['year', 'life_expectancy', 'bmi', 'thinness_10-19_years', 'thinness_5-9_years', 'income_composition_of_resources', 'schooling', 'alcohol']
    non_normal_cols = ['infant_deaths', 'measles', 'under-five_deaths', 'percentage_expenditure', 'hiv/aids', 'population']
    platykurtic_cols = ['polio', 'diphtheria', 'gdp', 'hepatitis_b']
    
    if len(normal_cols) > 0:
        st.write("Distribuição Normal:")
        plot_histograms(df, normal_cols, 'blue')

    if len(non_normal_cols) > 0:
        st.write("Distribuição Não-Normal:")
        plot_histograms(df, non_normal_cols, 'red')

    if len(platykurtic_cols) > 0:
        st.write("Distribuição Platicúrtica:")
        plot_histograms(df, platykurtic_cols, 'green')

    # Resultado dos outliers
    st.subheader("Outliers")
    outliers_info = {}
    for column in df_numeric.columns:
        values = df_numeric[column].dropna()
        if len(values) > 0:
            q75, q25 = np.percentile(values, [75, 25])
            iqr = q75 - q25

            min_val = q25 - (iqr * 1.5)
            max_val = q75 + (iqr * 1.5)

            outliers = np.where((values > max_val) | (values < min_val))[0]
            num_outliers = len(outliers)
            percent_outliers = num_outliers * 100 / len(values)

            outliers_info[column] = (num_outliers, round(percent_outliers, 2))
        else:
            outliers_info[column] = (0, 0.0)

    outliers_df = pd.DataFrame({'Nome da coluna': outliers_info.keys(), 'N° de de Outliers': [t[0] for t in outliers_info.values()], 'Porcentagem outliers (%)': [f"{t[1]:.2f}%" for t in outliers_info.values()]})
    st.dataframe(outliers_df)

<<<<<<< HEAD

=======
>>>>>>> 497de222b3214f116a644598e657e2dfcedc28df
def plot_histograms(df, columns, color):
    num_rows = 2 if len(columns) > 3 else 1
    num_cols = 4 if len(columns) > 3 else len(columns)
    fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(16, 8))
    for i, col in enumerate(columns):
        row_idx = i // num_cols
        col_idx = i % num_cols
        sns.histplot(df[col], kde=True, color=color, bins=30, ax=axes[row_idx, col_idx])
        axes[row_idx, col_idx].set_xlabel(col)
        axes[row_idx, col_idx].set_ylabel('Frequência')
        axes[row_idx, col_idx].set_title(f'Distribuição de {col}')
    plt.tight_layout()
    st.pyplot(fig)

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

def get_skew_kurtosis(df):
    skewness = df.apply(pd.Series.skew)
    kurtosis = df.apply(pd.Series.kurtosis)
    results_df = pd.DataFrame({'Assimetria': skewness, 'Curtose': kurtosis})
    return results_df
<<<<<<< HEAD


=======
>>>>>>> 497de222b3214f116a644598e657e2dfcedc28df

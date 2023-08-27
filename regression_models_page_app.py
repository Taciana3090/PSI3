import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from catboost import CatBoostRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt

@st.cache_data  
def load_data():
    df_final = pd.read_csv('C:/Users/tacia/Documents/PROJETO III/PSI3/data/df_final_tratado.csv')
    return df_final


def preprocess_data(df_final):
    df_final = df_final.drop(columns=['country', 'year'])
    # features (X) e o target (y)
    X = df_final.drop(columns=['life_expectancy'])
    y = df_final['life_expectancy']
    # one-hot encoding na coluna 'status'
    categorical_features = ['status']
    ct = ColumnTransformer([('onehot', OneHotEncoder(), categorical_features)], remainder='passthrough')
    X_encoded = ct.fit_transform(X)
    return X_encoded, y

# página de modelos de regressão
def regression_models_page():
    st.title("Análise de Modelos de Regressão para Previsão da Expectativa de Vida")
    df_final = load_data()
    X, y = preprocess_data(df_final)

    # modelos
    models = [
        ('CatBoost', CatBoostRegressor(verbose=False)),
        ('Linear Regression', LinearRegression()),
        ('Random Forest', RandomForestRegressor())
    ]

    # selecionar o modelo
    selected_model = st.selectbox("Selecione um modelo", [model_name for model_name, _ in models])
    selected_model_obj = None
    for model_name, model_obj in models:
        if model_name == selected_model:
            selected_model_obj = model_obj
            break

    if selected_model_obj is None:
        return
    # conjunto de treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    selected_model_obj.fit(X_train, y_train)
    # predição
    y_pred = selected_model_obj.predict(X_test)

 
    # mostrar métricas
    show_metrics = st.checkbox("Mostrar Métricas")
    if show_metrics:
        available_metrics = {
        "MSE": "Mean Squared Error é a média dos erros ao quadrado entre os valores reais e previstos.",
        "MAE": "Mean Absolute Error é a média dos valores absolutos dos erros entre os valores reais e previstos.",
        "RMSE": "Root Mean Squared Error é a raiz quadrada da média dos erros ao quadrado entre os valores reais e previstos.",
        "R-squared (R²)": "R-squared mede a proporção da variabilidade total dos valores dependentes que é explicada pelo modelo. Um valor mais próximo de 1 indica um bom ajuste."
    }
        selected_metrics = st.multiselect("Selecione as métricas a serem mostradas", list(available_metrics.keys()))
        for metric in selected_metrics:
            st.markdown(f"**{metric}**: {available_metrics[metric]}")
            if metric == "MSE":
                mse = mean_squared_error(y_test, y_pred)
                st.write(f"MSE: {mse}")
            elif metric == "MAE":
                mae = mean_absolute_error(y_test, y_pred)
                st.write(f"MAE: {mae}")
            elif metric == "RMSE":
                rmse = mean_squared_error(y_test, y_pred, squared=False)
                st.write(f"RMSE: {rmse}")
            elif metric == "R-squared (R²)":
                r2 = r2_score(y_test, y_pred)
                st.write(f"R-squared (R²): {r2}")

        # exibição de pontos no gráfico entre valores reais e previstos
    display_option = st.radio("Exibir pontos no gráfico:", ["Todos", "100 primeiros"])
    plt.figure(figsize=(20, 8))
    if display_option == "Todos":
        plt.plot(y_pred, label='Valor Predito', marker='*')
        plt.plot(y_test.to_numpy(), label='Valor Real', marker='o')
    else:  # "100 primeiros" é escolhido
        plt.plot(y_pred[:100], label='Valor Predito (100 primeiros)', marker='*')
        plt.plot(y_test[:100].to_numpy(), label='Valor Real (100 primeiros)', marker='o')
    plt.title(f'Comparação entre Valores Reais e Previstos - {selected_model}', fontsize=15)
    plt.xlabel('Amostras')
    plt.ylabel('Valor')
    plt.legend()
    plt.subplots_adjust(hspace=0.5)  
    st.pyplot()


def main():
    regression_models_page()

if __name__ == "__main__":
    main()

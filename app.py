# importando as bibliotecas necessárias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import altair as alt
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from datetime import datetime
import plotly.express as px

@st.cache_resource
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

file_path = "https://github.com/Taciana3090/PSI3/raw/Taciana3090/master/data/Life%20Expectancy%20Data.csv"
df = load_data(file_path)

# Centraliza o título utilizando HTML
st.write("<h1 style='text-align: center;'>Dashboard Life Expectancy</h1>", unsafe_allow_html=True)
st.write("""
Este dashboard tem como objetivo apresentar uma análise dos dados sobre o dataset Life Expectancy. 
""")

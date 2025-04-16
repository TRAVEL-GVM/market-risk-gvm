# main.py

import streamlit as st
import pandas as pd

st.set_page_config(page_title="S&P 500", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("dados/sp500.csv")
    return df

st.title("📈 S&P 500 - Dados Yahoo Finance")

df = load_data()
st.dataframe(df, use_container_width=True)

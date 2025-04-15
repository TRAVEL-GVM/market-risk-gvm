# get_data.py

import yfinance as yf
import pandas as pd
import os

def extract_data():
    ticker = "^GSPC"  # S&P 500
    df = yf.download(ticker, period="60d", interval="1d")
    os.makedirs("dados", exist_ok=True)
    df.to_csv("dados/sp500.csv")
    print("Dados atualizados com sucesso!")

if __name__ == "__main__":
    extract_data()

import pandas as pd

def load_data():
    df = pd.read_csv("banks.csv")
    return df

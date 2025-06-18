import pandas as pd

def load_csv():
    df = pd.read_csv("data/ventas.csv")
    print("Primeras filas del CSV:\n", df.head())
    print("\nÚltimas filas:\n", df.tail(3))
    print("\nInfo general:")
    print(df.info())
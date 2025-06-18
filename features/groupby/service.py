import pandas as pd
import numpy as np

def groupby_operations():
    df = pd.read_csv("data/ventas.csv")
    df['TotalVenta'] = df['Cantidad'] * df['Precio']
    print("Total venta por cliente:\n", df.groupby("Nombre")["TotalVenta"].sum())

    # NaN example
    data_nan = {'A': [1, np.nan], 'B': [np.nan, 2]}
    df_nan = pd.DataFrame(data_nan)
    print("\nCon NaN:\n", df_nan)
    print("Relleno con 0:\n", df_nan.fillna(0))
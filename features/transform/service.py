import pandas as pd
import numpy as np

def apply_transformations():
    df = pd.read_csv("data/ventas.csv")
    df['TotalVenta'] = df['Cantidad'] * df['Precio']
    df['CategoriaPrecio'] = np.select(
        [df['Precio'] < 50, (df['Precio'] >= 50) & (df['Precio'] < 200), df['Precio'] >= 200],
        ['Bajo', 'Medio', 'Alto'],
        default='Desconocido'
    )
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    print("DataFrame transformado:\n", df.head())
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def advanced_ops():
    df = pd.read_csv("data/ventas.csv")
    df['TotalVenta'] = df['Cantidad'] * df['Precio']
    df['Fecha'] = pd.to_datetime(df['Fecha'])

    df['DiaSemana'] = df['Fecha'].dt.day_name()
    print("Con día de semana:\n", df[['Nombre', 'Fecha', 'DiaSemana']])

    ventas_prod = df.groupby("Producto")["TotalVenta"].sum()
    ventas_prod.plot(kind="bar", title="Ventas por Producto")
    plt.show()
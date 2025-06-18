import pandas as pd

def merge_examples():
    clientes = pd.DataFrame({
        'ID_Cliente': [1, 2],
        'Nombre': ['Ana', 'Luis']
    })
    pedidos = pd.DataFrame({
        'ID_Pedido': [101, 102],
        'ID_Cliente': [1, 2],
        'Producto': ['Laptop', 'Mouse']
    })
    df = pd.merge(clientes, pedidos, on="ID_Cliente", how="inner")
    print("Inner merge:\n", df)
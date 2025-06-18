import pandas as pd

def create_dataframes():
    data = {
        'Nombre': ['Alice', 'Bob', 'Charlie'],
        'Edad': [25, 30, 22],
        'Ciudad': ['NY', 'LA', 'Chicago']
    }
    df = pd.DataFrame(data)
    print("DataFrame desde diccionario:\n", df)

    print("\nAcceder a columna 'Nombre':")
    print(df['Nombre'])

    print("\nFila con iloc[0]:")
    print(df.iloc[0])
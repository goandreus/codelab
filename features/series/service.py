import pandas as pd

def create_series():
    data_list = [10, 20, 30, 40, 50]
    s_from_list = pd.Series(data_list)
    print("Serie desde lista:\n", s_from_list)

    data_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
    s_from_dict = pd.Series(data_dict)
    print("\nSerie desde diccionario:\n", s_from_dict)

    print("\nElemento índice 0:", s_from_list[0])
    print("Elemento con etiqueta 'b':", s_from_dict['b'])

    s1 = pd.Series([1, 2, 3])
    s2 = pd.Series([4, 5, 6])
    print("\nSuma de series:\n", s1 + s2)
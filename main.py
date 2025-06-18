
from features.series import controller as series
from features.dataframes import controller as dataframes
from features.file_io import controller as file_io
from features.transform import controller as transform
from features.groupby import controller as groupby
from features.merge import controller as merge
from features.advanced import controller as advanced

def menu():
    while True:
        print("\n📘 Menú de Ejecución por Feature:")
        print("1. Series")
        print("2. DataFrames")
        print("3. Carga de Archivos")
        print("4. Transformaciones")
        print("5. Agrupaciones y NaN")
        print("6. Merge y Remodelación")
        print("7. Avanzado: Funciones, Fechas y Visualización")
        print("0. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            series.run()
        elif opcion == "2":
            dataframes.run()
        elif opcion == "3":
            file_io.run()
        elif opcion == "4":
            transform.run()
        elif opcion == "5":
            groupby.run()
        elif opcion == "6":
            merge.run()
        elif opcion == "7":
            advanced.run()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()

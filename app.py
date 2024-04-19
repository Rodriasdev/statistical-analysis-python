import pandas as pd

edades = [19,29,19,22,23,19,30,19,19,19,20,20,20,18,22,19,34,34,21,21,22,28,29,19
        ,20,19,25,28,21,22]

def analisis_estadistico(lista): 
    try:
        if not isinstance(lista, list):
            raise TypeError("El valor de entrada debe ser una lista.")
        
        if len(lista) == 0:
            print("La lista no debe estar vacía.")
            return
        
   
        if not all(isinstance(x, (int, float)) for x in lista):
            raise TypeError("Todos los elementos de la lista tienen que ser númericos.")
        
        data = pd.Series(lista)
        df = pd.DataFrame({"edades": dict(data.value_counts()).keys(), "fi": dict(data.value_counts()).values()})

        df["Fi"] = df['fi'].cumsum()

        df["ri"] = (df["fi"] / df["fi"].sum()).round(4)

        df["Ri"] = df['ri'].cumsum()

        df["pi%"] = df['ri'] * 100

        df["Pi%"] = df['Ri'] * 100

        print(df)
    except TypeError as e:
        print('Error:', e)

analisis_estadistico(edades)
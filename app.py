import pandas as pd

# Creamos un array con las edades
edades = [19,29,19,22,23,19,30,19,19,19,20,20,20,18,22,19,34,34,21,21,22,28,29,19
        ,20,19,25,28,21,22]

# Creamos una funcion que reciba una lista como parametro
def analisis_estadistico(lista): 
    # Agregamos el manejo de errores
    try:
        # Verificamos si el valor de entrada es una lista, si no es una lista mostramos un TypeError.
        if not isinstance(lista, list):
            raise TypeError("El valor de entrada debe ser una lista.")
        
        # Verificamos si la lista esta vacía, si esta vacía entonces retornamos un print.
        if len(lista) == 0:
             return print("La lista no debe estar vacía.")
           
        
        # Verificamos si todos los elementos de la lista son númericos, si no lo son entonces mostramos un TypeError.
        if not all(isinstance(x, (int, float)) for x in lista):
            raise TypeError("Todos los elementos de la lista tienen que ser númericos.")
        
        # Guardamos la lista en un objeto de pandas de tipo series y le asignamos el valor a data.
        data = pd.Series(lista)

        # Creamos un DataFrame en donde sacamos los valores unicos y calculamos el "fi" de la variable data, y las guardamos en sus columnas correspondientes.
        df = pd.DataFrame({"edades": dict(data.value_counts()).keys(), "fi": dict(data.value_counts()).values()})

        #Creamos una columna "FI" y lo calculamos.
        df["Fi"] = df['fi'].cumsum()

         #Creamos una columna "ri" y lo calculamos.
        df["ri"] = (df["fi"] / df["fi"].sum()).round(4)

         #Creamos una columna "Ri" y lo calculamos.
        df["Ri"] = df['ri'].cumsum()

         #Creamos una columna "pi%" y lo calculamos.
        df["pi%"] = df['ri'] * 100

         #Creamos una columna "Pi%" y lo calculamos.
        df["Pi%"] = df['Ri'] * 100

        # Retornamos el DataFrame
        return df, print(df)
    except TypeError as e:
        print('Error:', e)

analisis_estadistico(edades)
import pandas as pd

data = [
['Alice', 25],
['Bob', 30],
['Charlie', 35]
]
df = pd.DataFrame(data, columns=['Nombre', 'Edad'])


data_frame = pd.read_csv("Libro1.csv", delimiter= ";")




data_frame["Fi"] = data_frame['fi'].cumsum()

data_frame["ri"] = (data_frame["fi"] / data_frame["fi"].sum()).round(4)

data_frame["Ri"] = data_frame['ri'].cumsum()

data_frame["pi%"] = data_frame['ri'] * 100

data_frame["Pi%"] = data_frame['Ri'] * 100

data_frame.to_clipboard(decimal=",")
print(data_frame)

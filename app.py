print("Hello World")
import pandas as pd

lista=[23,45,7,34,6,63,36,78,54,34]
serie=pd.Series(lista)
"""serie=pd.Series([23,45,7,34,6,63,36,78,54,34])"""
print(serie)
fechas=pd.date_range(start='2021-05-01',end='2021-05-12')
print(fechas)

my_series = pd.Series([2, 4, 6, 8, 10])

def dividir(x):
    return x/2

"""print(my_series.apply(lambda x: x/2))"""
"""print(my_series.apply(dividir))"""

"""data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porsche", "Cayenne", "White"]]
frame=pd.DataFrame(data,columns=['Brand','Model','Color'])
print(frame)"""

data = [
    { 
        "brand": "Toyota", 
        "model": "Corolla",
        "color": "Blue"
    },
    {
        "brand": "Ford", 
        "model": "K",
        "color": "Yellow"
    },
    {
        "brand": "Porsche", 
        "model": "Cayenne",
        "color": "White"
    },
    {
        "brand": "Tesla", 
        "model": "S",
        "color": "Red"
    }
]

frame=pd.DataFrame(data)
print(frame)

data_frame=pd.read_csv('.learn/assets/pokemon_data.csv')
"""print(data_frame.iloc[133,6])
print(data_frame.head(3))
print(data_frame.tail(3))
print(data_frame[['Name','Type 1']][0:10])
print("aidwujawiudawd")
print(data_frame.loc[data_frame['Attack'] > 80])"""

print(len(data_frame.loc[data_frame['Legendary'] == True]))

bebe=pd.read_csv('.learn/assets/us_baby_names_right.csv')
print(bebe.head())
del bebe[bebe.columns[0]]
print(bebe)

print("adsdfargaefawefawefawe")

print(bebe.value_counts('Gender'))

suma=bebe.groupby("Name").sum()
print(len(suma))
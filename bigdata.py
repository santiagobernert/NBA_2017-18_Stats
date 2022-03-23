from jugador import Jugador
import os, pandas as pd

#carpeta = os.path.dirname('G:/Otros ordenadores/Mi PC/app/Python/data science/nba/')

carpeta = os.path.dirname('C:/Users/Profesores/Documents/gringo/NBA_2017-18_Stats/')

#leer archivo csv
df = pd.read_csv(f'{carpeta}/NBA Players Stats 201718.csv')

#lista de todos los jugadores
jugadores = []
for i in range(664):
    j = Jugador(*df.iloc[i])
    jugadores.append(j)
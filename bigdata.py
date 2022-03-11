from jugador import Jugador
import os, pandas as pd

carpeta = os.path.dirname('G:/Otros ordenadores/Mi PC/app/Python/data science/nba/')

df = pd.read_csv(f'{carpeta}/NBA Players Stats 201718.csv')

jugadores = []
for i in range(664):
    j = Jugador(*df.iloc[i])
    jugadores.append(j)
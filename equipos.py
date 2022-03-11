from jugador import Jugador
import pandas as pd, os


carpeta = os.path.dirname('E:/Santi/app/Python/data science/nba/')

df = pd.read_csv(f'{carpeta}/NBA Players Stats 201718.csv')

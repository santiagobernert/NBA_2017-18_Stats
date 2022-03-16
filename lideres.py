from jugador import Jugador
from bigdata import jugadores as jg, df

def lideres(estadistica):
    resultados = []
    df.sort_values(estadistica)
    rank_lideres = [*df.iloc[[0, 1, 2, 3, 4], [0]]]
    for i in range(len(jg)-10):
        if jg[i].rank in rank_lideres:
            resultados.append[i]
    return resultados

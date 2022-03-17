from jugador import Jugador
from bigdata import jugadores as jg, df

def lideres(estadistica):
    resultados = []
    df.sort_values(estadistica)
    rank_lideres = [ *df.iloc
    for i in jg:
        if i.rank in rank_lideres:
            resultados.append(i)
    print(rank_lideres)
    print (i.nombre for i in resultados)
    return resultados

lideres('BLK')

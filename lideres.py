from jugador import Jugador
from bigdata import jugadores as jg, df

def lideres(estadistica):
    resultados = []
    rank_lideres = [ *df.sort_values(estadistica, ascending=False).head(5)['Rk'] ]
    for i in range(len(rank_lideres)):
        for j in jg:
            if j.rank == rank_lideres[i]:
                resultados.append(j)
    print(rank_lideres)
    for i in resultados:
        print(f'{i.nombre}: {estadistica}')
    return resultados

#lideres('BLK')

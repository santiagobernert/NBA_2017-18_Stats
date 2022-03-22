from jugador import Jugador
from bigdata import jugadores as jg, df

# funcion que devuelve la lista de los 5 jugadores lideres en la estadistica seleccionada
def lideres(estadistica):
    if estadistica != 'Seleccionar':
        resultados = []
        if estadistica == '3P%':
            rank_lideres = [ *df[df['3P'] >= 2].sort_values(estadistica, ascending=False).head(5)['Rk'] ]
        elif estadistica == 'FG%':
            rank_lideres = [ *df[df['FG'] >= 5].sort_values(estadistica, ascending=False).head(5)['Rk'] ]
        else:
            rank_lideres = [ *df.sort_values(estadistica, ascending=False).head(5)['Rk'] ]
        for i in range(len(rank_lideres)):
            for j in jg:
                if j.rank == rank_lideres[i]:
                    resultados.append(j)
        for i in resultados:
            print(f'{i.nombre}: {estadistica}')
        return resultados

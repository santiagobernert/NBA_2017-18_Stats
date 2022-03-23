from jugador import Jugador
from bigdata import jugadores as jg, df

# funcion que devuelve la lista de los 5 jugadores lideres en la estadistica seleccionada
def equipo(estadistica):
    if estadistica != 'Seleccionar':
        resultados = []
        posiciones = ['PG', 'SG', 'SF', 'PF', 'C']
        if estadistica == '3P%':
            rank_lideres = [ *df[df['3P'] >= 2].sort_values(estadistica, ascending=False).head(200)['Rk'] ]
        elif estadistica == 'FG%':
            rank_lideres = [ *df[df['FG'] >= 5].sort_values(estadistica, ascending=False).head(200)['Rk'] ]
        else:
            rank_lideres = [ *df.sort_values(estadistica, ascending=False).head(200)['Rk'] ]
        for i in range(len(rank_lideres)):
            print(posiciones[0])
            for j in jg:
                if len(posiciones) >= 2:
                    if j.rank == rank_lideres[i] and j.pos == posiciones[0]:
                        resultados.append(j)
                        posiciones.remove(j.pos)
        for i in resultados:
            print(f'{i.nombre}: {i.pos}')
            
        return resultados

equipo('PTS')
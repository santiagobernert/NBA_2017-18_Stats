from jugador import Jugador
from bigdata import jugadores as jg, df

# funcion que devuelve la lista de los 5 jugadores lideres en la estadistica seleccionada
def equipo(estadistica):
    if estadistica != 'Seleccionar':
        resultados = ['1','2', '3', '4', '5']
        posiciones = ['PG', 'SG', 'SF', 'PF', 'C']
        posiciones_restantes = ['PG', 'SG', 'SF', 'PF', 'C']
        if estadistica == '3P%':
            rank_lideres = [ *df[df['3P'] >= 2].sort_values(estadistica, ascending=False)['Rk'] ]
        elif estadistica == 'FG%':
            rank_lideres = [ *df[df['FG'] >= 5].sort_values(estadistica, ascending=False)['Rk'] ]
        else:
            rank_lideres = [ *df.sort_values(estadistica, ascending=False)['Rk'] ]
        for i in rank_lideres:
            for j in jg:
                if len(posiciones_restantes) >= 1:
                    if j.rank == i and j.pos in posiciones_restantes:
                        resultados.pop(posiciones.index(j.pos))
                        resultados.insert(posiciones.index(j.pos), j)
                        posiciones_restantes.remove(j.pos)
        for i in resultados:
            print(f'{i.rank}  {i.nombre}: {i.pos} {i.reb}')
            
        return resultados

equipo('TRB')
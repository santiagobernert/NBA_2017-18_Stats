import jyserver.Flask as jsf
from bigdata import jugadores as jg, df


equipos = {
    'atlanta hawks': 'ATL',
    'boston celtics': 'BOS',
    'brooklyn nets': 'BRK',
    'charlotte hornets': 'CHO',
    'chicago bulls': 'CHI',
    'cleveland cavaliers': 'CLE',
    'dallas mavericks': 'DAL',
    'denver nuggets': 'DEN',
    'detroit pistons': 'DET',
    'golden state warriors': 'GSW',
    'houston rockets': 'HOU',
    'indiana pacers': 'IND',
    'los angeles clippers': 'LAC',
    'los angeles lakers': 'LAL',
    'memphis grizzlies': 'MEM',
    'miami heat': 'MIA',
    'milwaukee bucks': 'MIL',
    'minnesota timberwolves': 'MIN',
    'new orleans pelicans': 'NOP',
    'new york knicks': 'NYK',
    'oklahoma thunder': 'OKC',
    'orlando magic': 'ORL',
    'philadelphia sixers': 'PHI',
    'phoenix suns': 'PHO',
    'portland trail blazers': 'POR',
    'sacramento kings': 'SAC',
    'san antonio spurs': 'SAS',
    'toronto raptors': 'TOR',
    'utah jazz': 'UTH',
    'washington wizards': 'WAS',
}

# posiciones
pos = {
    'Todas':'PG SG SF PF C',
    'Base': 'PG',
    'Escolta': 'SG',
    'Alero': 'SF',
    'Ala-Pivot': 'PF', 
    'Pivot': 'C'
}


# buscar jugador en la lista de jugadores de bigdata
def buscar_jug():
    equipo = str(input('Equipo: '))       #str(App.input_equipos.value)
    posicion = str(input('Posicion: '))      #App.js.document.getElementById('sel-posicion')
    nombre = str(input('Nombre: '))        #App.js.document.getElementById('search-input')

    for i in jg:
        if nombre.upper() in i.nombre.upper() and i.pos in pos[posicion] and equipo.upper() in i.equipo:
            print('Jugador encontrado')
            print(i.nombre, i.pos, i.equipo, i.pts)
        elif equipo.upper() != '' and equipo.upper() in i.equipo:
            if pos[posicion] in i.pos:
                print(f'Todos los {posicion} de {equipo}')
                print(i.nombre, i.pos, i.equipo, i.pts)
            else:
                print('Jugadores de: ', equipo)
                print(i.nombre, i.pos, i.equipo, i.pts)
        elif i.pos in pos[posicion] and equipo == '':
            print('Todos los ', posicion)
            print(i.nombre, i.pos, i.equipo, i.pts)



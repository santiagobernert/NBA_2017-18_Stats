from flask import Flask, render_template, request
import jyserver.Flask as jsf
from jugador import Jugador
from bigdata import jugadores as jg, df
from buscar import equipos, jugadores, pos




nombre_jugador = 'Davis'

app = Flask(__name__)

@jsf.use(app)
class App:
    def __init__(self):
        pass
    
    def buscar_jugador(self):
        resultados = []
        resultados.clear()
        equipo = str(self.js.document.getElementById('equipo-search-input').value)
        posicion = str(self.js.document.getElementById('sel-posicion').value)
        nombre = str(self.js.document.getElementById('search-input').value)

        for i in range(1, 10):
            self.js.document.getElementById(f'jug{i}').style.visibility = 'visible'

        for i in jg:
            if nombre != '' and nombre.upper() in i.nombre.upper():# and i.pos in pos[posicion] and equipos[equipo.lower()] in i.equipo:
                if equipo != 'Todos' and equipos[equipo.lower()] in i.equipo:
                    self.js.console.log(f'Jugador de {equipo} encontrado')
                    self.js.console.log(i.nombre, i.pos, i.equipo, i.pts)
                    resultados.append(i)
                elif posicion != 'Todas' and i.pos in pos[posicion]:
                    self.js.console.log(f'{posicion} encontrado')
                    self.js.console.log(i.nombre, i.pos, i.equipo, i.pts)
                    resultados.append(i)
                elif posicion == 'Todas' and equipo == 'Todos':
                    self.js.console.log('Jugador encontrado')
                    self.js.console.log(i.nombre, i.pos, i.equipo, i.pts)
                    resultados.append(i)
            elif nombre == '' and equipo != 'Todos' and equipos[equipo.lower()] in i.equipo and pos[posicion] in i.pos:
                self.js.console.log(f'Todos los {posicion} de {equipo}')
                self.js.console.log(i.nombre, i.pos, i.equipo, i.pts)
                resultados.append(i)
            elif nombre == '' and equipo != 'Todos' and equipos[equipo.lower()] in i.equipo and posicion == 'Todas':
                self.js.console.log('Jugadores de: ', equipo)
                self.js.console.log(i.nombre, i.pos, i.equipo, i.pts)
                resultados.append(i)
            elif nombre == '' and i.pos in pos[posicion]:
                if equipo == 'Todos':
                    self.js.console.log('Todos los ', posicion)
                    self.js.console.log(i.nombre, i.pos, i.equipo, i.pts)
                    resultados.append(i)
        
        if len(resultados) == 0:
            self.js.document.getElementById('nombre_jugador_2').innerHTML = 'No se encontró al jugador'
            self.js.document.getElementById('ppg2').style.visibility = 'hidden'
            self.js.document.getElementById('apg2').style.visibility = 'hidden'
            self.js.document.getElementById('rpg2').style.visibility = 'hidden'
            self.js.document.getElementById('jug1').style.visibility = 'hidden'
            self.js.document.getElementById('jug3').style.visibility = 'hidden'
            self.js.document.getElementById('jug4').style.visibility = 'hidden'
            self.js.document.getElementById('jug5').style.visibility = 'hidden'
            self.js.document.getElementById('jug6').style.visibility = 'hidden'
            self.js.document.getElementById('jug7').style.visibility = 'hidden'
            self.js.document.getElementById('jug8').style.visibility = 'hidden'
            self.js.document.getElementById('jug9').style.visibility = 'hidden'
        
        elif len(resultados) == 1:
            self.js.document.getElementById('nombre_jugador_2').innerHTML = resultados[0].nombre
            self.js.document.getElementById('ppg2').innerHTML = resultados[0].pts
            self.js.document.getElementById('apg2').innerHTML = resultados[0].ast
            self.js.document.getElementById('rpg2').innerHTML = resultados[0].reb
            self.js.document.getElementById('jug1').style.visibility = 'hidden'
            self.js.document.getElementById('jug3').style.visibility = 'hidden'
            self.js.document.getElementById('jug4').style.visibility = 'hidden'
            self.js.document.getElementById('jug5').style.visibility = 'hidden'
            self.js.document.getElementById('jug6').style.visibility = 'hidden'
            self.js.document.getElementById('jug7').style.visibility = 'hidden'
            self.js.document.getElementById('jug8').style.visibility = 'hidden'
            self.js.document.getElementById('jug9').style.visibility = 'hidden'
            
        elif len(resultados) == 2:
            self.js.document.getElementById('nombre_jugador_2').innerHTML = resultados[0].nombre
            self.js.document.getElementById('ppg2').innerHTML = resultados[0].pts
            self.js.document.getElementById('apg2').innerHTML = resultados[0].ast
            self.js.document.getElementById('rpg2').innerHTML = resultados[0].reb
            self.js.document.getElementById('nombre_jugador_5').innerHTML = resultados[1].nombre
            self.js.document.getElementById('ppg5').innerHTML = resultados[1].pts
            self.js.document.getElementById('apg5').innerHTML = resultados[1].ast
            self.js.document.getElementById('rpg5').innerHTML = resultados[1].reb
            self.js.document.getElementById('jug1').style.visibility = 'hidden'
            self.js.document.getElementById('jug3').style.visibility = 'hidden'
            self.js.document.getElementById('jug4').style.visibility = 'hidden'
            self.js.document.getElementById('jug6').style.visibility = 'hidden'
            self.js.document.getElementById('jug7').style.visibility = 'hidden'
            self.js.document.getElementById('jug8').style.visibility = 'hidden'
            self.js.document.getElementById('jug9').style.visibility = 'hidden'
                
        elif len(resultados) == 3:
            self.js.document.getElementById('nombre_jugador_2').innerHTML = resultados[0].nombre
            self.js.document.getElementById('ppg2').innerHTML = resultados[0].pts
            self.js.document.getElementById('apg2').innerHTML = resultados[0].ast
            self.js.document.getElementById('rpg2').innerHTML = resultados[0].reb
            self.js.document.getElementById('nombre_jugador_5').innerHTML = resultados[1].nombre
            self.js.document.getElementById('ppg5').innerHTML = resultados[1].pts
            self.js.document.getElementById('apg5').innerHTML = resultados[1].ast
            self.js.document.getElementById('rpg5').innerHTML = resultados[1].reb
            self.js.document.getElementById('nombre_jugador_8').innerHTML = resultados[2].nombre
            self.js.document.getElementById('ppg8').innerHTML = resultados[2].pts
            self.js.document.getElementById('apg8').innerHTML = resultados[2].ast
            self.js.document.getElementById('rpg8').innerHTML = resultados[2].reb
            self.js.document.getElementById('jug1').style.visibility = 'hidden'
            self.js.document.getElementById('jug3').style.visibility = 'hidden'
            self.js.document.getElementById('jug4').style.visibility = 'hidden'
            self.js.document.getElementById('jug6').style.visibility = 'hidden'
            self.js.document.getElementById('jug7').style.visibility = 'hidden'
            self.js.document.getElementById('jug9').style.visibility = 'hidden'

        elif len(resultados) == 4:
            self.js.document.getElementById('nombre_jugador_1').innerHTML = resultados[0].nombre
            self.js.document.getElementById('ppg1').innerHTML = resultados[0].pts
            self.js.document.getElementById('apg1').innerHTML = resultados[0].ast
            self.js.document.getElementById('rpg1').innerHTML = resultados[0].reb
            self.js.document.getElementById('nombre_jugador_2').innerHTML = resultados[1].nombre
            self.js.document.getElementById('ppg2').innerHTML = resultados[1].pts
            self.js.document.getElementById('apg2').innerHTML = resultados[1].ast
            self.js.document.getElementById('rpg2').innerHTML = resultados[1].reb
            self.js.document.getElementById('nombre_jugador_3').innerHTML = resultados[2].nombre
            self.js.document.getElementById('ppg3').innerHTML = resultados[2].pts
            self.js.document.getElementById('apg3').innerHTML = resultados[2].ast
            self.js.document.getElementById('rpg3').innerHTML = resultados[2].reb
            self.js.document.getElementById('nombre_jugador_5').innerHTML = resultados[3].nombre
            self.js.document.getElementById('ppg5').innerHTML = resultados[3].pts
            self.js.document.getElementById('apg5').innerHTML = resultados[3].ast
            self.js.document.getElementById('rpg5').innerHTML = resultados[3].reb
            self.js.document.getElementById('jug4').style.visibility = 'hidden'
            self.js.document.getElementById('jug6').style.visibility = 'hidden'
            self.js.document.getElementById('jug7').style.visibility = 'hidden'
            self.js.document.getElementById('jug8').style.visibility = 'hidden'
            self.js.document.getElementById('jug9').style.visibility = 'hidden'

        elif len(resultados) == 5:
            self.js.document.getElementById('nombre_jugador_1').innerHTML = resultados[0].nombre
            self.js.document.getElementById('ppg1').innerHTML = resultados[0].pts
            self.js.document.getElementById('apg1').innerHTML = resultados[0].ast
            self.js.document.getElementById('rpg1').innerHTML = resultados[0].reb
            self.js.document.getElementById('nombre_jugador_2').innerHTML = resultados[1].nombre
            self.js.document.getElementById('ppg2').innerHTML = resultados[1].pts
            self.js.document.getElementById('apg2').innerHTML = resultados[1].ast
            self.js.document.getElementById('rpg2').innerHTML = resultados[1].reb
            self.js.document.getElementById('nombre_jugador_3').innerHTML = resultados[2].nombre
            self.js.document.getElementById('ppg3').innerHTML = resultados[2].pts
            self.js.document.getElementById('apg3').innerHTML = resultados[2].ast
            self.js.document.getElementById('rpg3').innerHTML = resultados[2].reb
            self.js.document.getElementById('nombre_jugador_4').innerHTML = resultados[3].nombre
            self.js.document.getElementById('ppg4').innerHTML = resultados[3].pts
            self.js.document.getElementById('apg4').innerHTML = resultados[3].ast
            self.js.document.getElementById('rpg4').innerHTML = resultados[3].reb
            self.js.document.getElementById('nombre_jugador_5').innerHTML = resultados[4].nombre
            self.js.document.getElementById('ppg5').innerHTML = resultados[4].pts
            self.js.document.getElementById('apg5').innerHTML = resultados[4].ast
            self.js.document.getElementById('rpg5').innerHTML = resultados[4].reb
            self.js.document.getElementById('jug6').style.visibility = 'hidden'
            self.js.document.getElementById('jug7').style.visibility = 'hidden'
            self.js.document.getElementById('jug8').style.visibility = 'hidden'
            self.js.document.getElementById('jug9').style.visibility = 'hidden'

        elif len(resultados) == 6:
            self.js.document.getElementById('nombre_jugador_1').innerHTML = resultados[0].nombre
            self.js.document.getElementById('ppg1').innerHTML = resultados[0].pts
            self.js.document.getElementById('apg1').innerHTML = resultados[0].ast
            self.js.document.getElementById('rpg1').innerHTML = resultados[0].reb
            self.js.document.getElementById('nombre_jugador_2').innerHTML = resultados[1].nombre
            self.js.document.getElementById('ppg2').innerHTML = resultados[1].pts
            self.js.document.getElementById('apg2').innerHTML = resultados[1].ast
            self.js.document.getElementById('rpg2').innerHTML = resultados[1].reb
            self.js.document.getElementById('nombre_jugador_3').innerHTML = resultados[2].nombre
            self.js.document.getElementById('ppg3').innerHTML = resultados[2].pts
            self.js.document.getElementById('apg3').innerHTML = resultados[2].ast
            self.js.document.getElementById('rpg3').innerHTML = resultados[2].reb
            self.js.document.getElementById('nombre_jugador_4').innerHTML = resultados[3].nombre
            self.js.document.getElementById('ppg4').innerHTML = resultados[3].pts
            self.js.document.getElementById('apg4').innerHTML = resultados[3].ast
            self.js.document.getElementById('rpg4').innerHTML = resultados[3].reb
            self.js.document.getElementById('nombre_jugador_5').innerHTML = resultados[4].nombre
            self.js.document.getElementById('ppg5').innerHTML = resultados[4].pts
            self.js.document.getElementById('apg5').innerHTML = resultados[4].ast
            self.js.document.getElementById('rpg5').innerHTML = resultados[4].reb
            self.js.document.getElementById('nombre_jugador_6').innerHTML = resultados[5].nombre
            self.js.document.getElementById('ppg6').innerHTML = resultados[5].pts
            self.js.document.getElementById('apg6').innerHTML = resultados[5].ast
            self.js.document.getElementById('rpg6').innerHTML = resultados[5].reb
            self.js.document.getElementById('jug7').style.visibility = 'hidden'
            self.js.document.getElementById('jug8').style.visibility = 'hidden'
            self.js.document.getElementById('jug9').style.visibility = 'hidden'

        elif len(resultados) == 7:
            self.js.document.getElementById('nombre_jugador_1').innerHTML = resultados[0].nombre
            self.js.document.getElementById('ppg1').innerHTML = resultados[0].pts
            self.js.document.getElementById('apg1').innerHTML = resultados[0].ast
            self.js.document.getElementById('rpg1').innerHTML = resultados[0].reb
            self.js.document.getElementById('nombre_jugador_2').innerHTML = resultados[1].nombre
            self.js.document.getElementById('ppg2').innerHTML = resultados[1].pts
            self.js.document.getElementById('apg2').innerHTML = resultados[1].ast
            self.js.document.getElementById('rpg2').innerHTML = resultados[1].reb
            self.js.document.getElementById('nombre_jugador_3').innerHTML = resultados[2].nombre
            self.js.document.getElementById('ppg3').innerHTML = resultados[2].pts
            self.js.document.getElementById('apg3').innerHTML = resultados[2].ast
            self.js.document.getElementById('rpg3').innerHTML = resultados[2].reb
            self.js.document.getElementById('nombre_jugador_4').innerHTML = resultados[3].nombre
            self.js.document.getElementById('ppg4').innerHTML = resultados[3].pts
            self.js.document.getElementById('apg4').innerHTML = resultados[3].ast
            self.js.document.getElementById('rpg4').innerHTML = resultados[3].reb
            self.js.document.getElementById('nombre_jugador_5').innerHTML = resultados[4].nombre
            self.js.document.getElementById('ppg5').innerHTML = resultados[4].pts
            self.js.document.getElementById('apg5').innerHTML = resultados[4].ast
            self.js.document.getElementById('rpg5').innerHTML = resultados[4].reb
            self.js.document.getElementById('nombre_jugador_6').innerHTML = resultados[5].nombre
            self.js.document.getElementById('ppg6').innerHTML = resultados[5].pts
            self.js.document.getElementById('apg6').innerHTML = resultados[5].ast
            self.js.document.getElementById('rpg6').innerHTML = resultados[5].reb
            self.js.document.getElementById('nombre_jugador_8').innerHTML = resultados[6].nombre
            self.js.document.getElementById('ppg8').innerHTML = resultados[6].pts
            self.js.document.getElementById('apg8').innerHTML = resultados[6].ast
            self.js.document.getElementById('rpg8').innerHTML = resultados[6].reb
            self.js.document.getElementById('jug7').style.visibility = 'hidden'
            self.js.document.getElementById('jug9').style.visibility = 'hidden'

        elif len(resultados) == 8:
            self.js.document.getElementById('nombre_jugador_1').innerHTML = resultados[0].nombre
            self.js.document.getElementById('ppg1').innerHTML = resultados[0].pts
            self.js.document.getElementById('apg1').innerHTML = resultados[0].ast
            self.js.document.getElementById('rpg1').innerHTML = resultados[0].reb
            self.js.document.getElementById('nombre_jugador_2').innerHTML = resultados[1].nombre
            self.js.document.getElementById('ppg2').innerHTML = resultados[1].pts
            self.js.document.getElementById('apg2').innerHTML = resultados[1].ast
            self.js.document.getElementById('rpg2').innerHTML = resultados[1].reb
            self.js.document.getElementById('nombre_jugador_3').innerHTML = resultados[2].nombre
            self.js.document.getElementById('ppg3').innerHTML = resultados[2].pts
            self.js.document.getElementById('apg3').innerHTML = resultados[2].ast
            self.js.document.getElementById('rpg3').innerHTML = resultados[2].reb
            self.js.document.getElementById('nombre_jugador_4').innerHTML = resultados[3].nombre
            self.js.document.getElementById('ppg4').innerHTML = resultados[3].pts
            self.js.document.getElementById('apg4').innerHTML = resultados[3].ast
            self.js.document.getElementById('rpg4').innerHTML = resultados[3].reb
            self.js.document.getElementById('nombre_jugador_5').innerHTML = resultados[4].nombre
            self.js.document.getElementById('ppg5').innerHTML = resultados[4].pts
            self.js.document.getElementById('apg5').innerHTML = resultados[4].ast
            self.js.document.getElementById('rpg5').innerHTML = resultados[4].reb
            self.js.document.getElementById('nombre_jugador_6').innerHTML = resultados[5].nombre
            self.js.document.getElementById('ppg6').innerHTML = resultados[5].pts
            self.js.document.getElementById('apg6').innerHTML = resultados[5].ast
            self.js.document.getElementById('rpg6').innerHTML = resultados[5].reb
            self.js.document.getElementById('nombre_jugador_7').innerHTML = resultados[6].nombre
            self.js.document.getElementById('ppg7').innerHTML = resultados[6].pts
            self.js.document.getElementById('apg7').innerHTML = resultados[6].ast
            self.js.document.getElementById('rpg7').innerHTML = resultados[6].reb
            self.js.document.getElementById('nombre_jugador_8').innerHTML = resultados[7].nombre
            self.js.document.getElementById('ppg8').innerHTML = resultados[7].pts
            self.js.document.getElementById('apg8').innerHTML = resultados[7].ast
            self.js.document.getElementById('rpg8').innerHTML = resultados[7].reb
            self.js.document.getElementById('jug9').style.visibility = 'hidden'

        elif len(resultados) >= 9:
            self.js.document.getElementById('nombre_jugador_1').innerHTML = resultados[0].nombre
            self.js.document.getElementById('ppg1').innerHTML = resultados[0].pts
            self.js.document.getElementById('apg1').innerHTML = resultados[0].ast
            self.js.document.getElementById('rpg1').innerHTML = resultados[0].reb
            self.js.document.getElementById('nombre_jugador_2').innerHTML = resultados[1].nombre
            self.js.document.getElementById('ppg2').innerHTML = resultados[1].pts
            self.js.document.getElementById('apg2').innerHTML = resultados[1].ast
            self.js.document.getElementById('rpg2').innerHTML = resultados[1].reb
            self.js.document.getElementById('nombre_jugador_3').innerHTML = resultados[2].nombre
            self.js.document.getElementById('ppg3').innerHTML = resultados[2].pts
            self.js.document.getElementById('apg3').innerHTML = resultados[2].ast
            self.js.document.getElementById('rpg3').innerHTML = resultados[2].reb
            self.js.document.getElementById('nombre_jugador_4').innerHTML = resultados[3].nombre
            self.js.document.getElementById('ppg4').innerHTML = resultados[3].pts
            self.js.document.getElementById('apg4').innerHTML = resultados[3].ast
            self.js.document.getElementById('rpg4').innerHTML = resultados[3].reb
            self.js.document.getElementById('nombre_jugador_5').innerHTML = resultados[4].nombre
            self.js.document.getElementById('ppg5').innerHTML = resultados[4].pts
            self.js.document.getElementById('apg5').innerHTML = resultados[4].ast
            self.js.document.getElementById('rpg5').innerHTML = resultados[4].reb
            self.js.document.getElementById('nombre_jugador_6').innerHTML = resultados[5].nombre
            self.js.document.getElementById('ppg6').innerHTML = resultados[5].pts
            self.js.document.getElementById('apg6').innerHTML = resultados[5].ast
            self.js.document.getElementById('rpg6').innerHTML = resultados[5].reb
            self.js.document.getElementById('nombre_jugador_7').innerHTML = resultados[6].nombre
            self.js.document.getElementById('ppg7').innerHTML = resultados[6].pts
            self.js.document.getElementById('apg7').innerHTML = resultados[6].ast
            self.js.document.getElementById('rpg7').innerHTML = resultados[6].reb
            self.js.document.getElementById('nombre_jugador_8').innerHTML = resultados[7].nombre
            self.js.document.getElementById('ppg8').innerHTML = resultados[7].pts
            self.js.document.getElementById('apg8').innerHTML = resultados[7].ast
            self.js.document.getElementById('rpg8').innerHTML = resultados[7].reb
            self.js.document.getElementById('nombre_jugador_9').innerHTML = resultados[8].nombre
            self.js.document.getElementById('ppg9').innerHTML = resultados[8].pts
            self.js.document.getElementById('apg9').innerHTML = resultados[8].ast
            self.js.document.getElementById('rpg9').innerHTML = resultados[8].reb

    def buscar_equipo(self):
        pass
                

@app.route('/', methods=['POST', 'GET'])
def home():
    return App.render(render_template('nba.html', nombre_jugador=nombre_jugador))

if __name__ == '__main__':
    app.run(debug=True)

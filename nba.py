from flask import Flask, render_template, request
import jyserver.Flask as jsf
from jugador import Jugador
from bigdata import jugadores as jg, df
from buscar import equipos, pos
from lideres import lideres


app = Flask(__name__)

@jsf.use(app)
class App:
    def __init__(self):
        self.resultados_buscar = []
        self.resultados_equipos = []
        self.resultados_lideres = []

    #mostrar resultados en la página
    def mostrar_resultados(self, box_jugador, resultados_index, page='', estadistica=''):
        resultados = []
        if page == '':
            resultados = self.resultados_buscar
        elif page == 'e':
            resultados = self.resultados_equipos
        elif page == 'l':
            resultados = self.resultados_lideres
        self.js.document.getElementById('jug'+ page + str(box_jugador)).style.visibility = 'visible'
        self.js.document.getElementById('nombre_jugador_'+ page + str(box_jugador)).innerHTML = resultados[resultados_index].nombre
        self.js.document.getElementById('ppg'+ page + str(box_jugador)).innerHTML = resultados[resultados_index].pts
        self.js.document.getElementById('apg'+ page + str(box_jugador)).innerHTML = resultados[resultados_index].ast
        self.js.document.getElementById('rpg'+ page + str(box_jugador)).innerHTML = resultados[resultados_index].reb

        if estadistica == 'FG%':
            if resultados[resultados_index].tiros_p >= resultados[resultados_index].ast:
                self.js.document.getElementById('apg'+ page + str(box_jugador)).innerHTML = resultados[resultados_index].tiros_p
            else:
                self.js.document.getElementById('rpg'+ page + str(box_jugador)).innerHTML = resultados[resultados_index].tiros_p
        elif estadistica == '3P':
            if resultados[resultados_index].triples_m >= resultados[resultados_index].ast:
                self.js.document.getElementById('apg'+ page + str(box_jugador)).innerHTML = resultados[resultados_index].triples_m
            else:
                self.js.document.getElementById('rpg'+ page + str(box_jugador)).innerHTML = resultados[resultados_index].triples_m
        elif estadistica == '3P%':
            if resultados[resultados_index].triples_p >= resultados[resultados_index].ast:
                self.js.document.getElementById('apg'+ page + str(box_jugador)).innerHTML = resultados[resultados_index].triples_p
            else:
                self.js.document.getElementById('rpg'+ page + str(box_jugador)).innerHTML = resultados[resultados_index].triples_p
        elif estadistica == 'BLK':
            if resultados[resultados_index].blk >= resultados[resultados_index].ast:
                self.js.document.getElementById('apg'+ page + str(box_jugador)).innerHTML = resultados[resultados_index].blk
            else:
                self.js.document.getElementById('rpg'+ page + str(box_jugador)).innerHTML = resultados[resultados_index].blk
        elif estadistica == 'STL':
            if resultados[resultados_index].stl >= resultados[resultados_index].ast:
                self.js.document.getElementById('apg'+ page + str(box_jugador)).innerHTML = resultados[resultados_index].stl
            else:
                self.js.document.getElementById('rpg'+ page + str(box_jugador)).innerHTML = resultados[resultados_index].stl
    
    
    
    #buscar jugador en la lista de jugadores de bigdata.py
    def buscar_jugador(self):
        self.resultados_buscar.clear()
        equipo = str(self.js.document.getElementById('equipo-search-input').value)
        posicion = str(self.js.document.getElementById('sel-posicion').value)
        nombre = str(self.js.document.getElementById('search-input').value)

        for i in range(1, 10):
            self.js.document.getElementById(f'jug{i}').style.visibility = 'hidden'

        for i in jg:
            if nombre != '' and nombre.upper() in i.nombre.upper():
                if equipo != 'Todos' and equipos[equipo.lower()] in i.equipo:
                    self.resultados_buscar.append(i)
                elif posicion != 'Todas' and i.pos in pos[posicion]:
                    self.resultados_buscar.append(i)
                elif posicion == 'Todas' and equipo == 'Todos':
                    self.resultados_buscar.append(i)
            elif nombre == '' and equipo != 'Todos' and equipos[equipo.lower()] in i.equipo and pos[posicion] in i.pos:
                self.resultados_buscar.append(i)
            elif nombre == '' and equipo != 'Todos' and equipos[equipo.lower()] in i.equipo and posicion == 'Todas':
                self.resultados_buscar.append(i)
            elif nombre == '' and i.pos in pos[posicion]:
                if equipo == 'Todos':
                    self.resultados_buscar.append(i)

        #mostrar en pantalla según la cantidad de resultados
        if len(self.resultados_buscar) == 0:
            self.js.document.getElementById('nombre_jugador_2').style.visibility = 'visible'
            self.js.document.getElementById('nombre_jugador_2').innerHTML = 'No se encontró al jugador'
        
        elif len(self.resultados_buscar) == 1:
            self.mostrar_resultados(2, 0)
            
        elif len(self.resultados_buscar) == 2:
            self.mostrar_resultados(2, 0)
            self.mostrar_resultados(5, 1)
                
        elif len(self.resultados_buscar) == 3:
            self.mostrar_resultados(2, 0)
            self.mostrar_resultados(5, 1)
            self.mostrar_resultados(8, 2)

        elif len(self.resultados_buscar) == 4:
            for i in range(len(resultados)-1):
                self.mostrar_resultados(i+1, i)
            self.mostrar_resultados(5, 3)

        elif len(self.resultados_buscar) == 5:
            for i in range(len(resultados)):
                self.mostrar_resultados(i+1, i)

        elif len(self.resultados_buscar) == 6:
            for i in range(len(resultados)):
                self.mostrar_resultados(i+1, i)

        elif len(self.resultados_buscar) == 7:
            for i in range(len(resultados)-1):
                self.mostrar_resultados(i+1, i)
            self.mostrar_resultados(8, 6)

        elif len(self.resultados_buscar) == 8:
            for i in range(len(resultados)):
                self.mostrar_resultados(i+1, i)

        elif len(self.resultados_buscar) >= 9:
            for i in range(9):
                self.mostrar_resultados(i+1, i)



    def buscar_lideres(self):
        estadistica = str(self.js.document.getElementById('sel-estadistica').value)
        self.resultados_lideres = lideres(estadistica)
        self.js.console.log(self.resultados_lideres)
        for i in range(6):
            if estadistica == 'STL' or estadistica == 'BLK' or estadistica == '3P' or estadistica == '3P%' or estadistica == 'FG%':
                self.mostrar_resultados(i, i+1, 'l', estadistica)
            else:
                self.mostrar_resultados(1, 0, 'l')
                

@app.route('/', methods=['POST', 'GET'])
def home():
    return App.render(render_template('nba.html'))

if __name__ == '__main__':
    app.run(debug=True)

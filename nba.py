from flask import Flask, render_template, request
import jyserver.Flask as jsf
from jugador import Jugador
from bigdata import jugadores as jg, df
from buscar import equipos, pos
from lideres import lideres




nombre_jugador = 'Davis'

app = Flask(__name__)

@jsf.use(app)
class App:
    def __init__(self):
        self.resultados_buscar = []
        self.resultados_equipos = []
        self.resultados_lideres = []

    def mostrar_resultados(self, box_jugador, resultados_index, page, estadistica=''):
        if page == 'b':
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
        if estadistica == '3P':
            if resultados[resultados_index].triples_m >= resultados[resultados_index].ast:
                self.js.document.getElementById('apg'+ page + str(box_jugador)).innerHTML = resultados[resultados_index].triples_m
            else:
                self.js.document.getElementById('rpg'+ page + str(box_jugador)).innerHTML = resultados[resultados_index].triples_m
        if estadistica == '3P%':
            if resultados[resultados_index].triples_p >= resultados[resultados_index].ast:
                self.js.document.getElementById('apg'+ page + str(box_jugador)).innerHTML = resultados[resultados_index].triples_p
            else:
                self.js.document.getElementById('rpg'+ page + str(box_jugador)).innerHTML = resultados[resultados_index].triples_p
        if estadistica == 'BLK':
            if resultados[resultados_index].blk >= resultados[resultados_index].ast:
                self.js.document.getElementById('apg'+ page + str(box_jugador)).innerHTML = resultados[resultados_index].blk
            else:
                self.js.document.getElementById('rpg'+ page + str(box_jugador)).innerHTML = resultados[resultados_index].blk
        if estadistica == 'STL':
            if resultados[resultados_index].stl >= resultados[resultados_index].ast:
                self.js.document.getElementById('apg'+ page + str(box_jugador)).innerHTML = resultados[resultados_index].stl
            else:
                self.js.document.getElementById('rpg'+ page + str(box_jugador)).innerHTML = resultados[resultados_index].stl
    
    def buscar_jugador(self):
        self.resultados.clear()
        equipo = str(self.js.document.getElementById('equipo-search-input').value)
        posicion = str(self.js.document.getElementById('sel-posicion').value)
        nombre = str(self.js.document.getElementById('search-input').value)

        for i in range(1, 10):
            self.js.document.getElementById(f'jug{i}').style.visibility = 'hidden'

        for i in jg:
            if nombre != '' and nombre.upper() in i.nombre.upper():# and i.pos in pos[posicion] and equipos[equipo.lower()] in i.equipo:
                if equipo != 'Todos' and equipos[equipo.lower()] in i.equipo:
                    self.resultados.append(i)
                elif posicion != 'Todas' and i.pos in pos[posicion]:
                    self.resultados.append(i)
                elif posicion == 'Todas' and equipo == 'Todos':
                    self.resultados.append(i)
            elif nombre == '' and equipo != 'Todos' and equipos[equipo.lower()] in i.equipo and pos[posicion] in i.pos:
                self.resultados.append(i)
            elif nombre == '' and equipo != 'Todos' and equipos[equipo.lower()] in i.equipo and posicion == 'Todas':
                self.resultados.append(i)
            elif nombre == '' and i.pos in pos[posicion]:
                if equipo == 'Todos':
                    self.resultados.append(i)

        
        if len(self.resultados) == 0:
            self.js.document.getElementById('jug2').style.visibility = 'visible'
            self.js.document.getElementById('nombre_jugador_2').innerHTML = 'No se encontró al jugador'
        
        elif len(self.resultados) == 1:
            self.mostrar_resultados(2, 0, 'b')
            
        elif len(self.resultados) == 2:
            self.mostrar_resultados(2, 0, 'b')
            self.mostrar_resultados(5, 1, 'b')
                
        elif len(self.resultados) == 3:
            self.mostrar_resultados(2, 0, 'b')
            self.mostrar_resultados(5, 1, 'b')
            self.mostrar_resultados(8, 2, 'b')

        elif len(self.resultados) == 4:
            self.mostrar_resultados(1, 0, 'b')
            self.mostrar_resultados(2, 1, 'b')
            self.mostrar_resultados(3, 2, 'b')
            self.mostrar_resultados(5, 3, 'b')

        elif len(self.resultados) == 5:
            self.mostrar_resultados(1, 0, 'b')
            self.mostrar_resultados(2, 1, 'b')
            self.mostrar_resultados(3, 2, 'b')
            self.mostrar_resultados(4, 3, 'b')
            self.mostrar_resultados(5, 4, 'b')

        elif len(self.resultados) == 6:
            self.mostrar_resultados(1, 0, 'b')
            self.mostrar_resultados(2, 1, 'b')
            self.mostrar_resultados(3, 2, 'b')
            self.mostrar_resultados(4, 3, 'b')
            self.mostrar_resultados(5, 4, 'b')
            self.mostrar_resultados(6, 5, 'b')

        elif len(self.resultados) == 7:
            self.mostrar_resultados(1, 0, 'b')
            self.mostrar_resultados(2, 1, 'b')
            self.mostrar_resultados(3, 2, 'b')
            self.mostrar_resultados(4, 3, 'b')
            self.mostrar_resultados(5, 4, 'b')
            self.mostrar_resultados(6, 5, 'b')
            self.mostrar_resultados(8, 6, 'b')

        elif len(self.resultados) == 8:
            self.mostrar_resultados(1, 0, 'b')
            self.mostrar_resultados(2, 1, 'b')
            self.mostrar_resultados(3, 2, 'b')
            self.mostrar_resultados(4, 3, 'b')
            self.mostrar_resultados(5, 4, 'b')
            self.mostrar_resultados(6, 5, 'b')
            self.mostrar_resultados(7, 6, 'b')
            self.mostrar_resultados(8, 7, 'b')

        elif len(self.resultados) >= 9:
            self.mostrar_resultados(1, 0, 'b')
            self.mostrar_resultados(2, 1, 'b')
            self.mostrar_resultados(3, 2, 'b')
            self.mostrar_resultados(4, 3, 'b')
            self.mostrar_resultados(5, 4, 'b')
            self.mostrar_resultados(6, 5, 'b')
            self.mostrar_resultados(7, 6, 'b')
            self.mostrar_resultados(8, 7, 'b')
            self.mostrar_resultados(9, 8, 'b')

    def buscar_equipo(self):
        pass

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
    return App.render(render_template('nba.html', nombre_jugador=nombre_jugador))

if __name__ == '__main__':
    app.run(debug=True)

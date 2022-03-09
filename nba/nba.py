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
        equipo = str(self.js.document.getElementById('equipo-search-input').value)
        posicion = str(self.js.document.getElementById('sel-posicion').value)
        nombre = str(self.js.document.getElementById('search-input').value)

        for i in jg:
            if nombre != '' and nombre.upper() in i.nombre.upper():# and i.pos in pos[posicion] and equipos[equipo.lower()] in i.equipo:
                self.js.console.log('Jugador encontrado')
                self.js.console.log(i.nombre, i.pos, i.equipo, i.pts)
            elif nombre != '' and equipo != 'Todos' and equipos[equipo.lower()] in i.equipo:
                if pos[posicion] in i.pos:
                    self.js.console.log(f'Todos los {posicion} de {equipo}')
                    self.js.console.log(i.nombre, i.pos, i.equipo, i.pts)
                else:
                    self.js.console.log('Jugadores de: ', equipo)
                    self.js.console.log(i.nombre, i.pos, i.equipo, i.pts)
            elif i.pos in pos[posicion] and equipo == 'Todos' and nombre == '':
                self.js.console.log('Todos los ', posicion)
                self.js.console.log(i.nombre, i.pos, i.equipo, i.pts)

    def buscar_equipo(self):
        pass
                

@app.route('/', methods=['POST', 'GET'])
def home():
    return App.render(render_template('nba.html', nombre_jugador=nombre_jugador))

if __name__ == '__main__':
    app.run(debug=True)

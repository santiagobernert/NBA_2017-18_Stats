# Clase Jugador
class Jugador:
    def __init__(self, rank, nombre, pos, edad, equipo, partidos, partidos_e, minutos, tiros_m,
                    tiros_i, tiros_p, triples_m, triples_i, triples_p, dobles_m, dobles_i,
                    dobles_p, efg, tl_m, tl_i, tl_p, rebo, rebd, reb, ast, rob, tap, perd, pf, pts):
        self.rank = rank
        self.nombre = nombre[:-10]
        self.pts = str(pts) + 'pts'
        self.reb = str(reb) + 'reb'
        self.ast = str(ast) + 'ast'
        self.pos = pos
        self.edad = edad
        self.equipo = equipo
        self.partidos = partidos
        self.partidos_e = partidos_e
        self.minutos = minutos
        self.tiros_m = tiros_m
        self.tiros_i = tiros_i
        self.tiros_p = str(tiros_p) + 'fg%'
        self.triples_m = str(triples_m) + ' 3p'
        self.triples_i = triples_i
        self.triples_p = str(triples_p) + ' 3p%'
        self.dobles_m = dobles_m
        self.dobles_i = dobles_i
        self.dobles_p = dobles_p
        self.efg = efg
        self.tl_m = tl_m
        self.tl_i = tl_i
        self.tl_p = tl_p
        self.rebo = rebo
        self.rebd = rebd
        self.rob = str(rob) + 'stl'
        self.tap = str(tap) + 'blk'
        self.perd = perd
        self.pf = pf
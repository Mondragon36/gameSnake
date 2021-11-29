from gameSnake.Dominio.jugador import Jugador
from gameSnake.Dominio.especificacion import Especificacion

class Registro:

    def __init__(self):
        self.jugadores = []

    def agregarJugador(self, jugador):
        if type(jugador) == Jugador:
            espec = Especificacion()
            espec.agregar_parametro('id', jugador.id)
            if len(list(self.buscar_jugador(espec))) == 0:
                self.jugadores.append(jugador)
            else:
                raise Exception('Jugador ya existe')

    def buscar_jugador(self, especificacion):
        for g in self.jugadores:
            if g.cumple(especificacion):
                yield g

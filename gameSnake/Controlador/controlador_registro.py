from gameSnake.Dominio.registro import Registro
from gameSnake.Infraestructura.persistencia_jugador import Persistencia_jugador

class Controlador_registro():
    def __init__(self):
        self.saverJugador = Persistencia_jugador()
        self.saverJugador.connect()

    def generarRegistro(self):
        registro = Registro()
        jugadores = self.saverJugador.consultar_tabla_jugador()

        for jugador in jugadores:
            registro.agregarJugador(jugador)
        return registro
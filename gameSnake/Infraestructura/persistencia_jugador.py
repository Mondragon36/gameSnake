import sqlite3

from gameSnake.Dominio import jugador
from gameSnake.Dominio.jugador import Jugador

class Persistencia_jugador():

    def __init__(self):
        self.connect()

    def connect(self):
        self.con = sqlite3.connect("snake.sqlite")
        print(self.con.cursor())
        self.__crear_tabla()

    def __crear_tabla(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE " \
                    "Jugador(" \
                    "id Integer PRIMARY KEY Autoincrement," \
                    "nombre text," \
                    "punto text," \
                    "record text)"
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar(self, jugador):
        cursor = self.con.cursor()
        query = "insert into Jugador" \
                "(id, " \
                "nombre, " \
                "punto, " \
                "record)" \
                "values(?,?,?,?)"
        cursor.execute(query, (jugador.id, jugador.nombre,
                               jugador.punto,
                               jugador.record))
        self.con.commit()

    def consultar_tabla_jugador(self):
        cursor = self.con.cursor()
        query = "SELECT * FROM Jugador"
        cursor.execute(query)
        rows = cursor.fetchall()
        return [Jugador(*row) for row in rows]

    def cargar_jugador(self, id):
        cursor = self.con.cursor()
        query = "SELECT id, nombre, punto , record FROM Jugador WHERE id=?"
        jugadores = cursor.execute(query, (id,))
        jugador_encontrado = None
        for id, nombre, punto, record in jugadores:
            jugador_encontrado = Jugador(id, nombre, punto, record)
        return jugador_encontrado

    def actualizar_jugador(self, jugador, id):
        query = 'UPDATE Jugador SET  nombre=? ,  punto=? , record=?' \
                'WHERE id=?'
        cursor = self.con.cursor()
        cursor.execute(query, (jugador.nombre,
                                jugador.punto,
                               jugador.record,
                               id))
        self.con.commit()
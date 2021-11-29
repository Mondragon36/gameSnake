class Jugador():
    def __init__(self, id, nombre, punto, record):
        self.id = id
        self.nombre = nombre
        self.punto = punto
        self.record = record

    def __repr__(self):
        representacion = "Jugador:" + " " + str(self.nombre) + " " + str(
            self.punto) + " " + "Id:" + " " + str(self.id)
        return representacion

    def cumple(self, especificacion):
        dict_jugador = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_jugador or dict_jugador[k] != especificacion.get_value(k):
                return False
        return True

    def _guardar(self, jugador) :
        from gameSnake.Infraestructura.persistencia_jugador import PersistenciaJugador
        persitencia_jugador = PersistenciaJugador()
        persitencia_jugador.guardar(jugador)

    def guardar_actualizar(self) :
        self._actualizar(self.id)

    def _actualizar(self, id) :
        from gameSnake.Infraestructura.persistencia_jugador import PersistenciaJugador
        persitencia_jugador = PersistenciaJugador()
        persitencia_jugador.actualizar_jugador(self, id)

    def  update(self,dict_params) :
        self.id = dict_params.get('id',self.id)
        self.nombre = dict_params.get('nombre',self.nombre)
        self.punto = dict_params.get('puntos',self.punto)
        self.record = dict_params.get('Record',self.record)

    def nuevoPunto(self, cambioPunto):
        self.punto = cambioPunto

    def nuevoRecord(self, cambioRecord):
        self.record = cambioRecord


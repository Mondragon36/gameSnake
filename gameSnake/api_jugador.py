import json

import falcon
import waitress
from falcon import App
from jsonpickle import json

from gameSnake.Dominio import jugador
from gameSnake.Dominio.jugador import Jugador
from gameSnake.Infraestructura.persistencia_jugador import Persistencia_jugador


class Obtener_jugador():
    def on_get(self,req,resp):
        db = Persistencia_jugador()
        auxs = db.consultar_tabla_jugador()
        resultado = []
        for aux in auxs:
            resultado.append(aux.__dict__)
        resp.body = json.dumps(resultado)
        resp.status = 200

class Api_jugador():

    def on_get(self,req,resp) :
        db= Persistencia_jugador()
        jugadores = db.consultar_tabla_jugador()
        template="""<!-- #######  YAY, I AM THE SOURCE EDITOR! #########-->
                        <h1 style="color: #5e9ca0;">Snake</h1>
                        <h2 style="color: #2e6c80;">Jugadores:</h2>
                        <h2 style="color: #2e6c80;">Cleaning options:</h2>
                        <table class="editorDemoTable" style="height: 362px;">
                        <thead>
                        <tr style="height: 18px;">
                        <td style="height: 18px; width: 263.172px;">Id</td>
                        <td style="height: 18px; width: 263.172px;">Nombre</td>
                        <td style="height: 18px; width: 348.625px;">Puntos </td>
                        <td style="height: 18px; width: 348.625px;">Record </td>
                        </tr>
                        </thead>
                        <tbody>
                    """
        for jugador in jugadores :
            jugador_template=f"""<tr style="height: 22px;">
                                    <td style="height: 22px; width: 263.172px;">{jugador.id}</td>
                                    <td style="height: 22px; width: 263.172px;">{jugador.nombre}</td>
                                    <td style="height: 22px; width: 348.625px;">{jugador.punto}</td>
                                    <td style="height: 22px; width: 348.625px;">{jugador.record}</td>                                
                                    </tr>
                                    """
            template += jugador_template
        template +="""</tbody>
        </table>"""
        resp.body=template
        resp.content_type='text/html'
        resp.status=falcon.HTTP_OK

    def on_post(self,req,resp) :
        jugador = Jugador(**req.media)
        jugador.guardar(jugador)
        resp.status=falcon.HTTP_CREATED

    def on_put(self,req,resp,id) :
        jugador_repositorio = Persistencia_jugador()
        jugador = jugador_repositorio.cargar_jugador(id)
        jugador.update(req.media)
        jugador.id = id
        jugador.guardar_actualizar()
        resp.body = jugador.__dict__

def iniciar(api) -> App:
    # run:app -b 0.0.0.0:2020 --workers 1 -t 240
    api.add_route("/jugador/",Api_jugador())
    api.add_route("/jugador_guardar/",Api_jugador())
    return api


import waitress
from falcon import App

from gameSnake.api_jugador import iniciar as jugador_routes


def iniciar() -> App:
    app = App()
    app = jugador_routes(app)
    return app

app = iniciar()

if __name__ == '__main__':
    waitress.serve(app, port=8080, url_scheme='http')
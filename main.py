import turtle
import time
import random

import jsonpickle

from gameSnake.Dominio.jugador import Jugador
from gameSnake.Dominio.registro import Registro

from gameSnake.Infraestructura.persistencia_jugador import Persistencia_jugador
from gameSnake.Dominio.especificacion import Especificacion
import requests


postpone=0.1

# marker
score=0
higth_score=0

windows=turtle.Screen()

# Screen
windows.title("Game snake")
windows.bgcolor("black")
windows.setup(width = 600,height = 600)
windows.tracer(0)

# Head snake
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("orange")
head.penup()
head.goto(0,0)
head.direction="stop"

# food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

# segment - body snake
segments=[]

# text
text=turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0,260)
text.write("Score: 0    high score: 0",align = "center",font = ("Courier",23,"normal"))


# funtiones

def up() :
    head.direction="up"


def down() :
    head.direction="down"


def left() :
    head.direction="left"


def rigth() :
    head.direction="Right"


def mov() :
    if head.direction == "up" :
        y=head.ycor()
        head.sety(y + 20)

    if head.direction == "down" :
        y=head.ycor()
        head.sety(y - 20)

    if head.direction == "left" :
        x=head.xcor()
        head.setx(x - 20)

    if head.direction == "Right" :
        x=head.xcor()
        head.setx(x + 20)

def generarUsuario(self):
    saverJugador = Persistencia_jugador()
    saverJugador.connect()
    registro = Registro()
    jugadores = saverJugador.consultar_tabla_jugador()
    for jugador in jugadores:
        registro .agregarJugador(jugador)
    return registro

# keyboard

windows.listen()
windows.onkeypress(up,"Up")
windows.onkeypress(down,"Down")
windows.onkeypress(left,"Left")
windows.onkeypress(rigth,"Right")

if __name__ == "__main__" :

    saverJugador = Persistencia_jugador
    saverJugador.connect()

    def cargarJugador():
        url = "hhtp://game--snake.herokuapp.com/index/"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        response = jsonpickle.loads(response.text)

        jugadores = []
        for i in range(len(response)):
            jugador = Jugador(response[i]["id"], response[i]["nombre"], response[i]["punto"], response[i]["record"])
            jugadores.append(jugador)

        return jugadores

    def generarJugador():
        registro = Registro()
        jugadores = cargarJugador()

        for jugador in jugadores:
            registro.agregarJugador(jugador)
        return registro

    def registroJugador():
        registro = Registro()
        id = str(input("Ingrese el id => "))
        nombre = str(input("Ingrese su nombre => "))
        punto = str(input("Ingrese su score => "))
        record = str(input("Ingrese su record => "))
        jugador = Jugador(id, nombre, punto, record)

        try:
            registro.agregarJugador(jugador)
            url = "hhtp://game--snake.herokuapp.com/jugador/"
            body = {
                "Id": id,
                "Nombre": nombre,
                "Score:": punto,
                "Record": record,
            }

            response = requests.request("POST", url, data=body)
            print(response.status_code)
            print("\n Se agrego a la db")
        except Exception as ex:
            print(ex)




    while True :
        windows.update()

        # edge of colisioens
        if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -298 :
            registro = Registro()
            id = str(input("Ingrese el id => "))
            nombre = str(input("Ingrese su nombre => "))
            punto = str(input("Ingrese su score => "))
            record = str(input("Ingrese su record => "))
            jugador = Jugador(id, nombre, punto, record)

            try:
                registro.agregarJugador(jugador)
                url = "hhtp://game-snake.herokuapp.com/resultado/"
                body = {
                    "Id": id,
                    "Nombre": nombre,
                    "Score:": punto,
                    "Record": record,
                }

                response = requests.request("POST", url, data=body)
                print(response.status_code)
                print("\n Se agrego a la db")
            except Exception as ex:
                print(ex)

            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"


            # delete segment
            for segment in segments :
                segment.goto(1000,1000)

            # clear list
            segments.clear()

            # resart marker
            score=0
            postpone=0.1
            text.clear()
            text.write(f"Score: {score}    high score: {higth_score}",align = "center",font = ("Courier",23,"normal"))

        # move food random
        if head.distance(food) < 20 :
            x=random.randint(-280,280)
            y=random.randint(-280,280)
            food.goto(x,y)

            new_segement=turtle.Turtle()
            new_segement.speed(0)
            new_segement.shape("square")
            new_segement.color("grey")
            new_segement.penup()
            segments.append(new_segement)

            # add marker
            score+=10
            postpone-=0.002
            if score > higth_score :
                higth_score=score

            text.clear()
            text.write(f"Score: {score}    high score: {higth_score}",align = "center",font = ("Courier",23,"normal"))

        # move the body snake
        totalSeg=len(segments)
        for index in range(totalSeg - 1,0,-1):
            x=segments [index - 1].xcor()
            y=segments [index - 1].ycor()
            segments [index].goto(x,y)

        if totalSeg > 0 :
            x=head.xcor()
            y=head.ycor()
            segments [0].goto(x,y)

        mov()
        # colisioens the body
        for segment in segments :
            if segment.distance(head) < 20:
                registro = Registro()
                id = str(input("Ingrese el id => "))
                nombre = str(input("Ingrese su nombre => "))
                punto = str(input("Ingrese su score => "))
                record = str(input("Ingrese su record => "))
                jugador = Jugador(id, nombre, punto, record)

                try:
                    registro.agregarJugador(jugador)
                    url = "hhtp://game-snake.herokuapp.com/resultado/"
                    body = {
                        "Id": id,
                        "Nombre": nombre,
                        "Score:": punto,
                        "Record": record,
                    }

                    response = requests.request("POST", url, data=body)
                    print(response.status_code)
                    print("\n Se agrego a la db")
                except Exception as ex:
                    print(ex)

                time.sleep(1)
                head.goto(0,0)
                head.direction="stop"

                # delete segment
                for segment in segments :
                    segment.goto(1000,1000)

                segments.clear()

                # resart marker
                score=0
                postpone=0.1
                text.clear()
                text.write(f"Score: {score}    high score: {higth_score}",align = "center",
                           font = ("Courier",23,"normal"))

        time.sleep(postpone)
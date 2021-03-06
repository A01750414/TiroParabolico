"""
Juego de tiro parabolico
Autores: Rafael Valenzuela Zurita, Victor Velazquez

"""
from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    """ Configura la accion de los clicks dentro de la ventana """
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 5
        speed.y = (y + 200) / 5


def inside(xy):
    " Devuelve True si el objeto esta dentro de la pantalla "
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    " Dibuja el proyectil y los objetivos "
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """ Desplaza el proyectil y los objetivos """
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 5

    if inside(ball):
        speed.y -= 4
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            target.x = 199

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()

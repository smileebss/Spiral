from turtle import *
from random import *
from math import *

def spiral(nb_circles, thickness, size):
    hideturtle()
    setheading(0)
    speed(10)
    penup()
    goto(0, 0)
    pendown()
    pensize(thickness)
    nb_actions = 360 * nb_circles
    for i in range(nb_actions):
        color(randint(0, 255), randint(0, 255), randint(0, 255))
        forward(i / size)
        left(1)

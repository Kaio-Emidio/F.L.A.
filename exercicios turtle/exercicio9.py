#1) Faça cada passo da tartaruga ter uma cor diferente

import turtle
import random

turtle = turtle.Turtle()
colors = ['purple', 'blue', 'pink', 'black']

for c in range(360):
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(1)
    turtle.right(1)

#2) Aumente/diminua o diâmetro do círculo

import turtle

turtle = turtle.Turtle()

for c in range(360):
    turtle.color('red')
    turtle.forward(2)
    turtle.right(1)
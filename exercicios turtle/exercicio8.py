#1) Acrescente cores

import turtle
import random

turtle = turtle.Turtle()

colors = ['purple', 'blue', 'yellow', 'green', 'pink', 'black', 'red']
for _ in range (8):
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(45)

#2) Mude a largura da linha

import turtle
import random

turtle = turtle.Turtle()
turtle.pensize(10)

colors = ['purple', 'blue', 'yellow', 'green', 'pink']
for _ in range (8):
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(45)

#3) Aumente a quantidade de linhas

import turtle
import random

turtle = turtle.Turtle()

colors = ['purple', 'blue', 'yellow', 'green', 'pink']
for _ in range (16):
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(24.5)
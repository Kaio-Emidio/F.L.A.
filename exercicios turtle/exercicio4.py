#1) Acrescente ao menos mais duas cores à lista de cores possíveis Veja os nomes de cores válidos em: https://pt.wikipedia.org/wiki/Lista_de_cores (coluna Nome Web)

import turtle
import random

turtle = turtle.Turtle()
colors = ['red', 'purple', 'blue', 'pink', 'black']

for _ in [1, 2, 3]:
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.right(120)

#2) Faça o triângulo apontar para cima

import turtle
import random

turtle = turtle.Turtle()
colors = ['red', 'purple', 'blue']

for _ in [1, 2, 3]:
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.left(120)

#3) Remova a cor vermelha da lista de cores possíveis

import turtle
import random

turtle = turtle.Turtle()
colors = ['purple', 'blue']

for _ in [1, 2, 3]:
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.right(120)

#4) Mude a largura da linha

import turtle
import random

turtle = turtle.Turtle()
colors = ['red', 'purple', 'blue']
turtle.pensize(10)

for _ in [1, 2, 3]:
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.right(120)
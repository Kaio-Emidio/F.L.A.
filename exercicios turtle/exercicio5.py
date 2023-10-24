#1) Aumente o tamanho do envelope

import turtle

turtle = turtle.Turtle()
turtle.color('red')

for _ in [1, 2, 3]:
    turtle.forward(200)
    turtle.right(120)

for _ in [1, 2, 3, 4]:
  turtle.forward(200)
  turtle.right(90)

#2) Use formas diferentes da tartaruga enquanto faz a aba e enquanto faz o corpo

import turtle

turtle = turtle.Turtle()
turtle.color('red')

turtle.shape('circle')
for _ in [1, 2, 3]:
    turtle.forward(100)
    turtle.right(120)

turtle.shape('square')
for _ in [1, 2, 3, 4]:
  turtle.forward(100)
  turtle.right(90)

#3) Deixe o envelope colorido

import turtle
import random

turtle = turtle.Turtle()
colors = ['red', 'purple', 'blue', 'pink', 'black']

for _ in [1, 2, 3]:
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.right(120)

for _ in [1, 2, 3, 4]:
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.right(90)

#4) Reduza o aba do envelope

import turtle

turtle = turtle.Turtle()
turtle.color('red')

turtle.forward(14.5)
for _ in [1, 2, 3]:
    turtle.forward(75)
    turtle.right(120)

turtle.backward(14.5)
for _ in [1, 2, 3, 4]:
  turtle.forward(100)
  turtle.right(90)
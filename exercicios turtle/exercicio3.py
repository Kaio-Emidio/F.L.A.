#1) Mude/defina a forma da tartaruga

import turtle

turtle = turtle.Turtle()
turtle.pensize(5)
turtle.shape("circle")

for color in ['blue', 'black', 'red', 'pink']:
    turtle.color(color)
    turtle.forward(100)
    turtle.right(90)

#2) Mude a ordem das cores

import turtle

turtle = turtle.Turtle()
turtle.pensize(5)

for color in ['black', 'blue', 'pink', 'red']:
    turtle.color(color)
    turtle.forward(100)
    turtle.right(90)

#3) Mude a largura da linha

import turtle

turtle = turtle.Turtle()
turtle.pensize(10)

for color in ['blue', 'black', 'red', 'pink']:
    turtle.color(color)
    turtle.forward(100)
    turtle.right(90)

#4) Faça a tartaruga desenhar dois quadrados

import turtle

turtle = turtle.Turtle()
turtle.pensize(5)

for _ in range(2):
    for color in ['blue', 'black', 'red', 'pink']:
        turtle.color(color)
        turtle.forward(100)
        turtle.right(90)
    turtle.left(90)
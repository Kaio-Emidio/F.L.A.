#1) Faça cada quadrado ter uma cor

import turtle

turtle = turtle.Turtle()

turtle.color('blue')
for _ in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.color('red')
for _ in range(4):
   turtle.left(90)
   turtle.forward(100)

turtle.color('green')
for _ in range(4):
   turtle.forward(100)
   turtle.left(90)

turtle.color('yellow')
for _ in range(4):
   turtle.right(90)
   turtle.forward(100)

#2) Faça cada quadrado com um formato diferente da tartaruga

import turtle

turtle = turtle.Turtle()

for _ in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.shape('square')
for _ in range(4):
   turtle.left(90)
   turtle.forward(100)

turtle.shape('turtle')
for _ in range(4):
   turtle.forward(100)
   turtle.left(90)

turtle.shape('circle')
for _ in range(4):
   turtle.right(90)
   turtle.forward(100)

#3) Faça os quadrados não se tocarem

import turtle

turtle = turtle.Turtle()

turtle.setx(50)
for _ in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.setx(-50)
turtle.sety(100)
for _ in range(4):
   turtle.left(90)
   turtle.forward(100)

turtle.setx(50)
for _ in range(4):
   turtle.forward(100)
   turtle.left(90)

turtle.sety(0)
turtle.setx(-50)
for _ in range(4):
   turtle.right(90)
   turtle.forward(100)

#4) Desenhe um quadrado maior ao redor dos demais quadrados

import turtle

turtle = turtle.Turtle()

for _ in range(4):
    turtle.forward(200)
    turtle.right(90)

for _ in range(4):
   turtle.left(90)
   turtle.forward(100)

for _ in range(4):
   turtle.forward(100)
   turtle.left(90)

for _ in range(4):
   turtle.right(90)
   turtle.forward(100)
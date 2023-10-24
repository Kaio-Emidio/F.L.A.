#1) Mude a distancia entre as lentes dos óculos

import turtle

turtle = turtle.Turtle()
turtle.color('green')

for _ in range(4):
    turtle.left(90)
    turtle.backward(100)

turtle.backward(200)
turtle.right(90)

for _ in range(3):
  turtle.forward(100)
  turtle.left(90)

#2) Mude o tamanho das lentes

import turtle

turtle = turtle.Turtle()
turtle.color('green')

for _ in range(4):
    turtle.left(90)
    turtle.backward(150)

turtle.backward(250)
turtle.right(90)

for _ in range(3):
  turtle.forward(150)
  turtle.left(90)
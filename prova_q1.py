lados = int(input("Digite o número de lados: "))
angulo = 360 / lados

import turtle
leo = turtle.Turtle()

for _ in range(lados):
    leo.forward(100)
    leo.right(angulo)
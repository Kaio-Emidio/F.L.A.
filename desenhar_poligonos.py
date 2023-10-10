
print("Informe o número de lados que o polígono terá")
lados = int(input("Número de lados: "))

angulo = 360 / lados

import turtle
leo = turtle.Turtle()
leo.penup()
leo.sety(300)
leo.pendown()

if lados > 2:
    for _ in range(lados):
        leo.forward(100)
        leo.right(angulo)
else:
    print("Número inválido, use um número maior ou igual a 3")
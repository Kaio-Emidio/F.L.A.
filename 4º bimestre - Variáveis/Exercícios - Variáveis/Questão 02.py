# Questão 02
# Adicione uma funcionalidade do seu programa que, quando o usuário apertar a tecla “Up” (seta para cima), o raio do círculo desenhado deverá aumentar em 5.

from turtle import Turtle, Screen, onscreenclick, onkey, listen
turtle = Turtle()
tela = Screen()

tamanho = 10

def mais():
    global tamanho
    tamanho += 5

def mov(x, y):
    turtle.penup()
    turtle.goto(x, y - tamanho)
    turtle.pendown()
    turtle.circle(tamanho)


onkey(mais, "Up")
onscreenclick(mov)

listen()
tela.mainloop()
# Questão 06
# Adicione uma funcionalidade no seu programa para, quando o usuário pressionar a tecla “-”, ele diminuir a espessura da linha em 1. A espessura não deverá ficar menor do que 1.

from turtle import Turtle, Screen, onscreenclick, onkey, listen
turtle = Turtle()
tela = Screen()

tamanho = 10
grossura = 1

def grosso():
    global grossura
    if grossura < 5:
        grossura += 1

def fino():
    global grossura
    if grossura > 1:
        grossura -= 1

def mais():
    global tamanho
    if tamanho < 30:
        tamanho += 5

def menos():
    global tamanho
    if tamanho > 5:
        tamanho -= 5

def mov(x, y):
    turtle.penup()
    turtle.goto(x, y - tamanho)
    turtle.pendown()
    turtle.pensize(grossura)
    turtle.circle(tamanho)

onkey(grosso, "+")
onkey(mais, "Up")
onkey(menos, "Down")
onscreenclick(mov)

listen()
tela.mainloop()
# Questão 08
# Adicione uma funcionalidade no seu programa para que ele alterne os desenhos entre Círculo e Triângulo.

from turtle import Turtle, Screen, onscreenclick, onkey, listen
turtle = Turtle()
tela = Screen()

tamanho = 10
grossura = 1
cor = 'Black'
forma = 1

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
    turtle.color(cor)
    turtle.pensize(grossura)
    if forma == 1:
        turtle.circle(tamanho)
    if forma == 2:
        for _ in range(3):
            turtle.forward(tamanho)
            turtle.left(120)

def R():
    global cor
    cor = 'Red'

def G():
    global cor
    cor = 'Green'

def B():
    global cor
    cor = 'Blue'

def C():
    global forma
    forma = 1
    return forma

def T():
    global forma
    forma = 2
    return forma

onkey(C, 'c')
onkey(T, 'q')
onkey(R, 'r')
onkey(G, 'g')
onkey(B, 'b')
onkey(grosso, "+")
onkey(fino, '-')
onkey(mais, "Up")
onkey(menos, "Down")
onscreenclick(mov)

listen()
tela.mainloop()
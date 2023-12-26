# Questão 10
# Altere o programa para que ele desenhe círculos apenas se o usuário clicar no quadrado definido pelos pontos (-250, -250) e (250, 250).

from turtle import Turtle, Screen, onscreenclick, onkey, listen
turtle = Turtle()
tela = Screen()

tamanho = 10
grossura = 1
cor = 'Black'
forma = 1

leo = Turtle()
leo.penup()
leo.goto(-250, -250)
leo.pendown()
for _ in range(4):
    leo.forward(500)
    leo.left(90)

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
    if forma == 1 and -250 < x < 250 and -250 < y < 250:
        turtle.circle(tamanho)
    if forma == 2:
        for _ in range(3):
            turtle.forward(tamanho*2)
            turtle.left(120)
    if forma == 3:
        for _ in range(4):
            turtle.forward(tamanho*2)
            turtle.left(90)

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

def Q():
    global forma
    forma = 3
    return forma

onkey(Q, 'q')
onkey(C, 'c')
onkey(T, 't')
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
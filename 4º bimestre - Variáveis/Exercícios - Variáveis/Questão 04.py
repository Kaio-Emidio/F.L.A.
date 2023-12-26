# Questão 04
# Altere a funcionalidade adicionada na questão 02 para que, caso o raio do círculo já seja igual a 30, não ocorra alteração no tamanho.

from turtle import Turtle, Screen, onscreenclick, onkey, listen
turtle = Turtle()
tela = Screen()

tamanho = 10

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
    turtle.circle(tamanho)

onkey(mais, "Up")
onkey(menos, "Down")
onscreenclick(mov)

listen()
tela.mainloop()
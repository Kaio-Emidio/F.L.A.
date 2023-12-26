# Questão 03
# Adicione uma funcionalidade do seu programa que, quando o usuário apertar a tecla “Down” (seta para baixo), o raio do círculo desenhado deverá diminuir em 5. Caso o valor do raio já seja 5, não deverá ocorrer nenhuma alteração.

from turtle import Turtle, Screen, onscreenclick, onkey, listen
turtle = Turtle()
tela = Screen()

tamanho = 10

def mais():
    global tamanho
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
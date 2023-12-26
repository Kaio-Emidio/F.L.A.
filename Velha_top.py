
from turtle import Turtle, Screen, onkey, onscreenclick, listen
turtle = Turtle()
tela = Screen()
tela.bgcolor('black')
turtle.speed(0)

def tabuleiro():
    turtle.color("white")
    for _ in range(4):
        for _ in range(4):
            turtle.forward(100)
            turtle.forward(-100)
            turtle.right(90)
        turtle.forward(100)
        turtle.right(90)

def xis():
    turtle.color('red')
    turtle.right(45)
    for _ in range(4):
        turtle.forward(50)
        turtle.forward(-50)
        turtle.right(90)
    turtle.left(45)

def bolinha():
    turtle.color('blue')
    x = turtle.xcor()
    y = turtle.ycor() - 45

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(45)

vez = 0
forma = 0

def alternar():
    global vez, forma
    vez = vez + 1
    forma = vez % 2

def jogada(x, y):
    global forma, vez

    turtle.penup()
    turtle.goto(x - (x % 100) + 50, y - (y % 100) + 50)
    turtle.pendown()

    alternar()

    if forma == 0:
        xis()
    if forma == 1:
        bolinha()

tabuleiro()
onscreenclick(jogada)
onkey(alternar, 'a')
listen()
tela.mainloop()
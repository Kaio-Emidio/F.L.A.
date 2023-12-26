from turtle import Turtle, onscreenclick, Screen
turtle = Turtle()
tela = Screen()

def circulo():
    turtle.circle(25)

def quadrado():
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)

def triangulo():
    for _ in range(3):
        turtle.forward(100)
        turtle.right(120)

def retangulo():
    for _ in range(2):
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)

def linha():
    turtle.forward(400)

for _ in range(4):
    linha()
    turtle.right(180)
    linha()
    turtle.right(90)

def desenho(x,y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    cordx = turtle.xcor()
    cordy = turtle.ycor()

    if cordx > 0 and cordy > 0:
        circulo()

    if cordx < 0 and cordy > 0:
        quadrado()

    if cordx < 0 and cordy < 0:
        triangulo()

    if cordx > 0 and cordy < 0:
        retangulo()

onscreenclick(desenho)

tela.mainloop()
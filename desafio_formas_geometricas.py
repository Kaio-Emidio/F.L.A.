import turtle
leo = turtle.Turtle()

def reta(a):
    leo.forward(a)

def quadrado(a):
    for _ in range(4):
        leo.forward(a)
        leo.right(90)

def triangulo(a):
    for _ in range(3):
        leo.forward(a)
        leo.right(120)

def retangulo(a,b):
    for _ in range(2):
        leo.forward(a)
        leo.right(90)
        leo.forward(b)
        leo.right(90)

def solzinho(a):
    for _ in range(20):
        leo.forward(a)
        leo.right(108)
        leo.forward(a)

def estrela(a):
    leo.setheading(63)
    for _ in range(5):
        leo.forward(a)
        leo.right(108)
        leo.forward(a)
        leo.left(36)

estrela(50)
from turtle import Turtle, onscreenclick, Screen
turtle = Turtle()
tela = Screen()
turtle.pensize(5)

def pos_v_init():
    turtle.penup()
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.pendown()

def pos_v_final():
    turtle.penup()
    turtle.right(90)
    turtle.forward(-25)
    turtle.left(90)
    turtle.pendown()

def pos_h_init():
    turtle.penup()
    turtle.forward(-25)
    turtle.pendown()

def pos_h_final():
    turtle.penup()
    turtle.forward(25)
    turtle.pendown()

def circulo():
    pos_v_init()
    turtle.circle(25)
    pos_v_final()

def triangulo():
    pos_h_init()
    pos_v_init()
    for _ in range(3):
        turtle.forward(50)
        turtle.left(120)
    pos_v_final()
    pos_h_final()

def quadrado():
    pos_h_init()
    pos_v_init()
    for _ in range(4):
        turtle.forward(50)
        turtle.left(90)
    pos_v_final()
    pos_h_final()

def xis():
    turtle.left(45)
    for _ in range(4):
        turtle.forward(25)
        turtle.left(180)
        turtle.forward(25)
        turtle.left(90)
    turtle.right(45)

def linha():
    turtle.forward(400)

for _ in range(4):
    linha()
    turtle.right(180)
    linha()
    turtle.right(90)

def goto_and_drawn(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

    x = turtle.xcor()
    y = turtle.ycor()

    if x > 0 and y > 0:
        turtle.penup()
        turtle.goto(x - (x % 50) + 25, y - (y % 50) + 25)
        turtle.pendown()
        turtle.pencolor('red')
        circulo()
    
    if x < 0 and y > 0:
        turtle.penup()
        turtle.goto((x+25)-x%50, (y+25)-y%50)
        turtle.pendown()
        turtle.pencolor('blue')
        quadrado()
    
    if x < 0 and y < 0:
        turtle.penup()
        turtle.goto((x+25)-x%50, (y+25)-y%50)
        turtle.pendown()
        turtle.pencolor('green')
        triangulo()

    if x > 0 and y < 0:
        turtle.penup()
        turtle.goto((x+25)-x%50, (y+25)-y%50)
        turtle.pendown()
        turtle.pencolor('yellow')
        xis()

onscreenclick(goto_and_drawn)

tela.mainloop()

# módulo de 50 para definir o inicio do quadrado e apartir dai ir para o meio
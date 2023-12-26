from turtle import Turtle, onscreenclick, onkey, onkeypress, listen, Screen, penup, pendown
turtle = Turtle()
tela = Screen()

def up():
    y_atual = turtle.ycor()
    novo_y = y_atual + 10
    turtle.sety(novo_y)

def down():
    y_atual = turtle.ycor()
    novo_y = y_atual - 10
    turtle.sety(novo_y)

def right():
    x_atual = turtle.xcor()
    novo_x = x_atual + 10
    turtle.setx(novo_x)

def left():
    x_atual = turtle.xcor()
    novo_x = x_atual - 10
    turtle.setx(novo_x)

def goto_and_mark(x, y):
   turtle.goto(x, y)
   turtle.write(turtle.position())

onscreenclick(goto_and_mark)
onkeypress(up, 'Up')
onkeypress(down, 'Down')
onkeypress(left, 'Left')
onkeypress(right, 'Right')
onkey(turtle.penup, 'u')
onkey(turtle.pendown, 'p')

listen()
tela.mainloop()
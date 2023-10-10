import turtle

leo = turtle.Turtle()

leo.penup()
leo.setx(-400)
leo.pendown()

def flor():
    for _ in range(6):
        for _ in range(8):
            leo.forward(20)
            leo.right(30)
        leo.right(60)

flor()

leo.penup()
leo.forward(300)
leo.pendown()

flor()

leo.penup()
leo.forward(300)
leo.pendown()

flor()
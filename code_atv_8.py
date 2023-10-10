import turtle
leo = turtle.Turtle()

def flor():
    for _ in range(6):
        for _ in range(8):
            leo.forward(20)
            leo.right(30)
        leo.right(60)

leo.up()
leo.goto(-250, 250)
leo.down()
flor()

leo.up()
leo.goto(0, 0)
leo.down()
flor()

leo.up()
leo.goto(250, -250)
leo.down()
flor()
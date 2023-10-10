import turtle
leo = turtle.Turtle()

def forma():
    for _ in range(6):
        leo.forward(25)
        leo.right(60)

def jump(a):
    leo.up()
    leo.forward(a)
    leo.down()

for _ in range(6):
    for _ in range(2):
        for _ in range(4):
            forma()
            jump(75)
        jump(-25)
        leo.right(60)
        jump(25)
        leo.right(120)
    jump(-25)
    leo.left(60)
    jump(50)
    leo.right(60)
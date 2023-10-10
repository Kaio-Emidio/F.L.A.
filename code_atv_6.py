import turtle
leo = turtle.Turtle()

for _ in range(12):
    for _ in range(2):
        leo.forward(60)
        leo.right(30)
        leo.forward(60)
        leo.right(150)
    leo.right(30)
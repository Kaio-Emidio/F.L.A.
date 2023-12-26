from turtle import Turtle, onscreenclick, Screen
turtle = Turtle()
tela = Screen()

def goto_and_mark(x, y):
   turtle.goto(x, y)
   turtle.write(turtle.position())

onscreenclick(goto_and_mark)

tela.mainloop()
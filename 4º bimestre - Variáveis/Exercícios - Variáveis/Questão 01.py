# Questão 01
# Utilizando a biblioteca Turtle, escreva um programa que, abra uma janela e quando um usuário clicar em algum ponto da tela, ele deverá desenhar um círculo de raio 10 no ponto clicado. O caminho percorrido pela tartura até chegar ao ponto clicado não deverá ser desenhado.

from turtle import Turtle, Screen, onscreenclick
turtle = Turtle()
tela = Screen()

def mov(x, y):
    turtle.penup()
    turtle.goto(x,y - 10)
    turtle.pendown()
    turtle.circle(10)

onscreenclick(mov)
tela.mainloop()
import turtle
leo = turtle.Turtle()

def quadrado():
    for _ in range(4):
        leo.forward(100)
        leo.right(90)

def circulo():
    leo.circle(50)

opção = ''

# forma, cor, velocidade, tamanho do pincel, posição

while opção != 0:
    print("1 - Círculo")
    print("2 - Quadrado")
    opção = int(input("Escolha o número referente a forma que deseja desenhar: "))
    
    cor = input("Digite em ingês a cor que quer seu desenho: ")
    velocidade = int(input("Digite a velocidade que você quer que a tartaruga desenhe: "))
    tamanho = int(input("Digite o tamanho do pincel que você quer: "))
    posx = float(input("Digite o valor da coordenada que quiser no eixo x: "))
    posy = float(input("Digite o valor da coordenada que quiser no eixo y: "))

    leo.color(cor)
    leo.speed(velocidade)
    leo.pensize(tamanho)
    leo.penup()
    leo.goto(posx, posy)
    leo.pendown()
    
    if opção == 1:
        circulo()
    if opção == 2:
        quadrado()

turtle.Screen().mainloop()
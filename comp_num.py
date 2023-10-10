print("Insira  três números:")
n1 = int(input("Valor 1: "))
n2 = int(input("Valor 2: "))
n3 = int(input("Valor 3: "))

if n1 > n2 > n3:
    print("O maior número é", n1, "e o menor é", n3)
if n1 > n3 > n2:
    print("O maior número é", n1, "e o menor é", n2)
if n2 > n1 > n3:
    print("O maior número é", n2, "e o menor é", n3)
if n2 > n3 > n1:
    print("O maior número é", n2, "e o menor é", n1)
if n3 > n1 > n2:
    print("O maior número é", n3, "e o menor é", n2)
if n3 > n2 > n1:
    print("O maior número é", n3, "e o menor é", n1)
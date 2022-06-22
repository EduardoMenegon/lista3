# 10) Faça um programa que leia uma matriz 3x3 de inteiros e multiplique
# os elementos da diagonal principal da matriz por um número k
# Imprima a matriz na tela antes e depois da multiplicação.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
m = int(input("Digite o número do multiplicador: "))

for x in range(3):
    for y in range(3):
        matriz[x][y] = (int(input("Digite o número da posição [{}][{}]: ".format(x, y))))
print("-"*30)
print("Matriz antes da multiplicação:")
print(matriz)
print("-"*30)
print("Matriz depois da multiplicação:")
for x in range(3):
    for y in range(3):
        if x == y:
            matriz[x][y] = matriz[x][y] * m
print(matriz)

# 11) Faça um programa que leia duas matrizes A e B 2x2 de inteiros
# e imprima a matriz C que é a soma das matrizes A e B.

matriz1 = [[0, 0], [0, 0]]
matriz2 = [[0, 0], [0, 0]]
matriz3 = [[0, 0], [0, 0]]
for x in range(2):
    for y in range(2):
        matriz1[x][y] = int(input("Digite o numero da posição [{}][{}] da primeira matriz: ".format(x, y)))
for x in range(2):
    for y in range(2):
        matriz2[x][y] = int(input("Digite o numero da posição [{}][{}] da segunda matriz: ".format(x, y)))
for x in range(2):
    for y in range(2):
        matriz3[x][y] = matriz1[x][y] + matriz2[x][y]
print(matriz3)

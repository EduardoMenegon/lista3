# 8) Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

name = str(input("Digite o nome: "))
for x in range(len(name)):
    print(name[x])

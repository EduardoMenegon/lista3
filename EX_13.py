# 13) Faça um programa para imprimir:
#  1
#  1 2
#  1 2 3
#  .....
#  1 2 3 ... n
# para um n informado pelo usuário. Use uma função que receba
# um valor n inteiro imprima até a enésima linha.

n = int(input("Digite o número desejado: "))
soma = ""
for i in range(1, n+1):
    numero = str(i)
    print(soma + numero)
    soma = soma + numero

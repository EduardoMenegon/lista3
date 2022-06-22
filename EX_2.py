# 2) Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma,
# a multiplicação e os números.

from math import prod
numeros = []
for x in range(1, 6):
    valor = int(input('Digite o valor' f" {x}: "))
    numeros.append(valor)
print('Os números são: ', numeros)
print('A soma dos números é ', sum(numeros))
print('O produto dos números é ', prod(numeros))

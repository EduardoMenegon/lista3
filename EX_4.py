# 4) Faça um Programa que leia um vetor A com 10 números inteiros,
# calcule e mostre a soma dos quadrados dos elementos do vetor.

soma = 0
for x in range(0, 10):
    y = int(input('Digite os números inteiros: '))
    soma = y*y + soma
print('A soma dos quadrados dos números digitados é: ', soma)

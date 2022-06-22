# 3) Faça um Programa que peça a idade e a altura de 5 pessoas,
# armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.

pessoas = []
idades = []
alturas = []
for x in range(1, 3):
    pessoas.append(str(input('Digite o nome da pessoa' f" {x}: ")))
    idades.append(int(input('Digite a idade da pessoa' f" {x}: ")))
    alturas.append(float(input('Digite a altura da pessoa' f" {x}: ")))
print(pessoas)
print(idades[::-1])
print(alturas[::-1])

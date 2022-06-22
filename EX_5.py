# 5) Faça um Programa que leia dois vetores com 10 elementos cada.
# Gere um terceiro vetor de 20 elementos, cujos valores deverão
# ser compostos pelos elementos intercalados dos dois outros vetores.

vetor1 = []
vetor2 = []
vetor3 = []

for x in range(1,11):
    a = []
    b = []
    a.append(int(input('Digite o valor' f" {x}"' para o primeiro vetor: ')))
    b.append(int(input('Digite o valor' f" {x}"' para o segundo vetor: ')))
    vetor1.append(a)
    vetor2.append(b)
    vetor3.append(a)
    vetor3.append(b)
print(vetor1)
print(vetor2)
print(vetor3)

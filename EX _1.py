# 1) Faça um Programa que peça as quatro notas de 10 alunos,
# calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

notas = []
media = 0
contador = 0
for x in range(1, 11):
    notas = []
    for y in range(1, 5):
        nota = float(input('Digite a nota' f" {y}" ' do aluno' f" {x} :"))
        notas.append(nota)
        media = sum(notas)/4
    if media >= 7:
        contador = contador + 1
print("Alunos a acima da média:", contador)

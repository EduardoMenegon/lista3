# 9) Nome na vertical em escada. Modifique o programa anterior de forma
# a mostrar o nome em formato de escada.

nome = str(input("Digite o nome: "))
base = ""
for i in range(len(nome)):
    print(base + nome[i])
    add = nome[i]
    base = base + add

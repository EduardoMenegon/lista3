# 16) Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
# taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo
# de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(x,y):
    valorfinal = x + x*y/100
    return valorfinal

x = int(input("Digite o valor do produto: R$"))
y = int(input("Digite a taxa do imposto: %"))
print(somaImposto(x, y))

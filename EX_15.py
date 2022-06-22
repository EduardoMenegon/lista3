# 15) Faça um programa, com uma função que necessite de um argumento.
# A função retorna o valor de caractere ‘P’, se seu argumento for
# positivo, e ‘N’, se seu argumento for zero ou negativo

def argumento(x):

    if x > 0:
        print("P")
    else:
        print("N")
    return ''

x = int(input("Digite o número: "))
print(argumento(x))
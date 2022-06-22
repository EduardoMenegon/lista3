# 14) Faça um programa, com uma função que necessite de três argumentos,
# e que forneça a soma desses três argumentos.
def soma(x, y, z):
    a = x + y + z
    return a

x =  int(input("Digite o primeiro número: "))
y =  int(input("Digite o segundo número: "))
z =  int(input("Digite o terceiro número: "))
print(soma(x, y, z))

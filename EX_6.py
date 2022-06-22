# 6) Faça um programa que leia 2 strings e informe o conteúdo delas
# seguido do seu comprimento. Informe também se as duas strings
# possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

string1 = str(input("Digite a primeira frase: "))
string2 = str(input("Digite a segunda frase: "))
x1 = len(string1)
x2 = len(string2)

if x1 == x2 and string1 == string2:
    print('"', string1, '"', "Possui {} caracteres.".format(x1))
    print('"', string2, '"', "Possui {} caracteres." .format(x2))
    print("As duas frases são do mesmo tamanho e possuem o mesmo conteúdo!")

elif string1 != string2 and x1 != x2:
    print('"', string1, '"', "Possui {} caracteres.".format(x1))
    print('"', string2, '"', "Possui {} caracteres.".format(x2))
    print("As frases possuem tamanhos e conteúdos diferentes!")
else:
    print('"', string1, '"', "Possui {} caracteres.".format(x1))
    print('"', string2, '"', "Possui {} caracteres.".format(x2))
    print("As frases possuem mesmo tamanho, mas conteúdos diferentes!")

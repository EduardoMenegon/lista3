# 18) Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no
# formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data
# seja inválida.

def data(dia,mes,ano):
    if dia > 30 or dia < 1:
        print("NULL")
    elif mes >12 or mes < 1:
        print("NULL")
    elif mes == 1:
        print(dia, " de janeiro de",ano)
    elif mes == 2:
        print(dia, " de fevereiro de",ano)
    elif mes == 3:
        print(dia, " de março de",ano)
    elif mes == 4:
        print(dia, " de abril de",ano)
    elif mes == 5:
        print(dia, " de maio de",ano)
    elif mes == 6:
        print(dia, " de junho de",ano)
    elif mes == 7:
        print(dia, " de julho de",ano)
    elif mes == 8:
        print(dia, " de agosto de",ano)
    elif mes == 9:
        print(dia, " de setembro de",ano)
    elif mes == 10:
        print(dia, " de outubro de",ano)
    elif mes == 11:
        print(dia, " de novembro de",ano)
    elif mes == 12:
        print(dia, " de dezembro de",ano)
    return ""

dia = int(input("Digite o dia de nascimento:"))
mes = int(input("Digite o mês de nascimento:"))
ano = int(input("Digite o ano de nascimento:"))

print(data(dia, mes, ano))
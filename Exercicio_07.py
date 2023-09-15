def dia_magico():
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mes: "))
    ano = input("Digite o ano: ")

    if (dia * mes) == int(ano[-2:]):
        print(f"Data mágica {dia}/{mes}/{ano}")
    else:
        print("Não é uma data mágica")

dia_magico()
def aptidao(num1, a):
    if a == "m" and num1 >= 60:
        return "Apto a doar"
    elif a == "f" and num1 >= 50:
        return "Apto a doar"
    else:
     return "Não Apto"

x = float(input("Digite seu peso: "))
y = (input("Digite seu gênero: ")).lower()

print(aptidao(x,y))
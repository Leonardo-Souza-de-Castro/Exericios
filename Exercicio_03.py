def multiplo(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False

print(multiplo(int(input("Digite um número: ")), int(input("Digite um número: "))))
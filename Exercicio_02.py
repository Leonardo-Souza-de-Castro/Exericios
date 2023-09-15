from Exercicio_01 import media

a = int(input("Digite um número: "))
b = int(input("Digite um número: "))

def maximo(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


print(maximo(a,b))
print(media(a,b))

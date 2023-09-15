from math import sqrt

def calc (n1, n2, n3):
    res = sqrt(n1) + sqrt(n2) + sqrt(n3) + ((n1+n2)/2) + ((n2+n3)/2) + ((n1+n3)/2)

    return res

a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int(input("Digite um número: "))


print(calc(a, b, c))
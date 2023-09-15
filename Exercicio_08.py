i = int(input("Digite um valor de 1 a 3: "))
a = float(input("Digite um valor: "))
b = float(input("Digite um valor: "))
c = float(input("Digite um valor: "))

valor1 = 0
valor2 = 0
valor3 = 0

def exibe (num1, x, y, z):

    if num1 == 1:
        if x > y:
            if x > z:
                valor1 = x
                if y > z:
                    valor2 = y
                    valor3 = z
                else:
                    valor2 = z
                    valor3 = y
            else:
                valor1 = z
                valor2 = x
                valor3 = y
        elif y > x:
            if y > z:
                valor1 = y
                if x > z:
                    valor2 = x
                    valor3 = z
                else:
                    valor2 = z
                    valor3 = x
            else:
                valor1 = z
                valor2 = y
                valor3 = x
        else:
            valor1 = z
            if x > y:
                valor2 = x
                valor3 = y
            else:
                valor2 = y
                valor3 = x
            
    if i == 2:
        if x < y:
            if x < z:
                valor1 = x
                if y < z:
                    valor2 = y
                    valor3 = z
                else:
                    valor2 = z
                    valor3 = y
            else:
                valor1 = z
                valor2 = x
                valor3 = y
        elif y < x:
            if y < z:
                valor1 = y
                if x < z:
                    valor2 = x
                    valor3 = z
                else:
                    valor2 = z
                    valor3 = x
            else:
                valor1 = z
                valor2 = y
                valor3 = x
        else:
            valor1 = z
            if x < y:
                valor2 = x
                valor3 = y
            else:
                valor2 = y
                valor3 = x

    else:
        if x > y:
            if x > z:
                valor1 = y
                valor2 = x
                valor3 = z
            else:
                valor1 = x
                valor2 = z
                valor3 = y
        else:
            if y > z:
                valor1 = x
                valor2 = y
                valor3 = z
            else:
                valor1 = x
                valor2 = z
                valor3 = y  
    print(valor1, valor2, valor3)
            

exibe(i,a,b,c)
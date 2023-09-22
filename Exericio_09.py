def calc_divi(num1, num2):
    count = 0
    while(True):
        num1 = num1 - num2
        count += 1

        if num1 < num2:
            print(f"O resultado é {count} e o resto é {num1}")
            break

a = int(input("Digite um número: "))
b = int(input("Digite um número: "))

calc_divi(a, b)
        
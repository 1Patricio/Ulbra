# Faça um programa para efetuar a leitura de quatro números e apresentar os números divisíveis por 2 e por 3.
num1 = float(input("Digite primeiro número: "))
num2 = float(input("Digite segundo número: "))
num3 = float(input("Digite terceiro número: "))
num4 = float(input("Digite quatro número: "))

if num1%2==0 and num1%3==0:
    print(f"{num1} é múltiplo de 2 e 3")
else:
    print(f"{num1} não é múltiplo de 2 e 3")

if num2%2==0 and num2%3==0:
    print(f"{num2} é múltiplo de 2 e 3")
else:
    print(f"{num2} não é múltiplo de 2 e 3")

if num3%2==0 and num3%3==0:
    print(f"{num3} é múltiplo de 2 e 3")
else:
    print(f"{num3} não é múltiplo de 2 e 3")

if num4%2==0 and num4%3==0:
    print(f"{num4} é múltiplo de 2 e 3")
else:
    print(f"{num4} não é múltiplo de 2 e 3")
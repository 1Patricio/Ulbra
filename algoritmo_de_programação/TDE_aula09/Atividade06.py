# Faça um programa para ler três valores quaisquer e escrever o maior dos 3.
num1 = float(input("Digite primeiro número: "))
num2 = float(input("Digite segundo número: "))
num3 = float(input("Digite terceiro número: "))

if num1 > num2 and num1>num3:
    print(f"{num1} é o maior número")
elif num2>num1 and num2>num3:
    print(f"{num2} é o maior número")
elif num3>num1 and num3>num2:
    print(f"{num3} é o maior número")
else:
    print("Os dois números são iguais")
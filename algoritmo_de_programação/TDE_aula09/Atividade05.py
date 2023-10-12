# Elabore um programa que lê dois valores e escreve cada um com a mensagem: “É múltiplo de 2” ou “Não é múltiplo de dois”
num1 = float(input("Digite primeiro número: "))
num2 = float(input("Digite segundo número: "))

if num1%2==0:
    print(f"{num1} é múltiplo de 2")
else:
    print(f"{num1} não é múltiplo de 2")

if num2%2==0:
    print(f"{num2} é múltiplo de 2")
else:
    print(f"{num2} não é múltiplo de 2")

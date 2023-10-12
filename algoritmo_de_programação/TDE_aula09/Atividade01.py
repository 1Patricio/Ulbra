# Elabore um programa que leia dois números e some 100 ao maior valor e apresente o resultado
num1 = float(input("Digite primeiro número: "))
num2 = float(input("Digite segundo número: "))

if num1 > num2:
    maior=num1+100
    print(f"Resultado: {maior}")
elif num2>num1:
    maior=num2+100
    print(f"Resultado: {maior}")
else:
    print("Os dois números são iguais")

    
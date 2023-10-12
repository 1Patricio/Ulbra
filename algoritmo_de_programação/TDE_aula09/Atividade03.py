# Faça um programa para ler dois valores numéricos e apresentar a diferença do maior pelo menor. 
num1 = float(input("Digite primeiro número: "))
num2 = float(input("Digite segundo número: "))

if num1 > num2:
    soma=num1-num2
    print(f"Resultado: {soma}")
elif num2>num1:
    soma=num2-num1
    print(f"Resultado: {soma}")
else:
    print("Os dois números são iguais")
# Faça um programa para ler dois números. Se os números forem iguais imprimir a mensagem: "NÚMEROS IGUAIS" e encerrar a execução; caso contrário, imprimir o de maior valor.
num1 = float(input("Digite primeiro número: "))
num2 = float(input("Digite segundo número: "))

if num1 > num2:
    print(f"{num1} é o maior número")
elif num2>num1:
    print(f"{num2} é o maior número")
else:
    print("Os dois números são iguais")
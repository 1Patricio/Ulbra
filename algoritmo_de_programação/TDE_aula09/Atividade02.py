# Faça um programa para determinar se uma pessoa é maior ou menor de idade.
idade = int(input("Digite sua idade: "))
if idade>=18:
    print(f"Você tem {idade} anos e já é maior de idade")
if idade<18:
    print(f"Você tem {idade} anos e é menor de idade")
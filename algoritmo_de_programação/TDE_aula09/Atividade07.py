# # Realize um programa que lê um conjunto de 4 valores i, a, b, c, onde i é um valor inteiro e positivo e a, b, c, são quaisquer valores reais e os escreva. A seguir:
# # Se i=1 escrever os 3 valores a, b, c em ordem crescente;
# # Se i=2 escrever os 3 valores a, b, c em ordem decrescente;
# # Se i=3 escrever os 3 valores de forma que o maior valor entre a, b, c fica entre os outros dois.

inteiro = int(input("Digite um valor de 1 a 3"))
num1 = float(input("Digite primeiro número: "))
num2 = float(input("Digite segundo número: "))
num3 = float(input("Digite terceiro número: "))

sorted(reversed)
print(f"{sorted}")

# if num1 > num2 and num1>num3:
#     maior=num1
# elif num2>num1 and num2>num3:
#     maior=num2
# # elif num3>num1 and num3>num2:
# else:
#     maior=num3

# if (num1>num2 and num1>num3) or (num1<num2 and num1<num3):
#     meio=num1
# elif num2>num1 and num2>num3 or (num2<num1 and num2<num3):
#     meio=num2
# # elif num3>num1 and num3<num2:
# else:
#     meio=num3

# if num1 < num2 and num1<num3:
#     menor=num1
# elif num2<num1 and num2<num3:
#     menor=num2
# # elif num3<num1 and num3<num2:
# else:
#     menor=num3
    
# if inteiro == 1:
#     print(f"{maior}, {meio}, {menor}")

# ------------------------------------

# inteiro = int(input("Digite um valor de 1 a 3: "))
# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))
# num3 = float(input("Digite o terceiro número: "))

if inteiro == 1:
    if num1 <= num2 <= num3:
        print(f"{num1}, {num2}, {num3}")
    elif num1 <= num3 <= num2:
        print(f"{num1}, {num3}, {num2}")
    elif num2 <= num1 <= num3:
        print(f"{num2}, {num1}, {num3}")
    elif num2 <= num3 <= num1:
        print(f"{num2}, {num3}, {num1}")
    elif num3 <= num1 <= num2:
        print(f"{num3}, {num1}, {num2}")
    else:
        print(f"{num3}, {num2}, {num1}")
# elif inteiro == 2:
#     if num1 >= num2 >= num3:
#         print(f"{num1}, {num2}, {num3}")
#     elif num1 >= num3 >= num2:
#         print(f"{num1}, {num3}, {num2}")
#     elif num2 >= num1 >= num3:
#         print(f"{num2}, {num1}, {num3}")
#     elif num2 >= num3 >= num1:
#         print(f"{num2}, {num3}, {num1}")
#     elif num3 >= num1 >= num2:
#         print(f"{num3}, {num1}, {num2}")
#     else:
#         print(f"{num3}, {num2}, {num1}")
elif inteiro == 3:
    lista = [num1, num2, num3]
    lista.sort()
    print(f"{lista[1]}, {lista[0]}, {lista[2]}")
else:
    print("Valor de i fora do intervalo permitido (1 a 3).")
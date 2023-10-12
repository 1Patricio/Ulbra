# Calcular e exibir o maior e menor de quatro números.
a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
c = int(input("Digite o terceiro número inteiro: "))
d = int(input("Digite o quarto número inteiro: "))

maiorA = a+1
menorA = a-1

maiorB = b+1
menorB = b-1

maiorC = c+1
menorC = c-1

maiorD = d+1
menorD = d-1

print(f"O menor e maior número de {a} é respectivamento {menorA} e {maiorA}\n")
print(f"O menor e maior número de {b} é respectivamento {menorB} e {maiorB}\n")
print(f"O menor e maior número de {c} é respectivamento {menorC} e {maiorC}\n")
print(f"O menor e maior número de {d} é respectivamento {menorD} e {maiorD}\n")
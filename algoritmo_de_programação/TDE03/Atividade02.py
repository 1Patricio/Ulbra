# Calcular e exibir o dobro de um número caso ele seja positivo.
numero = float(input("Digite um número: "))

if numero > 0:
    dobro = numero*2
    print(f"O número {numero} é positivo e o seu dobro é {dobro}")
else:
    print(f"O número {numero} não é positivo        ")
    
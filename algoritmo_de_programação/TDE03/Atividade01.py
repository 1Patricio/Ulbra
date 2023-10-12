# Verificar se um número é positivo, negativo ou zero.
numero = float(input("Digite um número: "))

if numero>0:
    print(f"O número {numero} é positivo ")

elif numero<0:
    print(f"O número {numero} é negativo ")
    
elif numero==0:
    print(f"O número {numero} é zero")
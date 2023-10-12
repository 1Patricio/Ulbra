# Verificar se um número é divisível por 3 e 5 ao mesmo tempo.
num = int(input("Digite um número inteiro: "))
if num%3==0 and num%5==0:
    print(f"O número {num} é divisível por 3 e por 5 ao mesmo tempo")    
else:
    print(f"O número {num} não é divisível por 3 e por 5 ao mesmo tempo")
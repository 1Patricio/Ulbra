# Verificar se um número é um quadrado perfeito.
num = int(input("Digite um número inteiro: "))

if (num%2==1 and num%8==1) or (num%4==0):
    print(f"O número {num} é um quadrado perfeito")
else:
    print(f"O número {num} não é um quadrado perfeito")
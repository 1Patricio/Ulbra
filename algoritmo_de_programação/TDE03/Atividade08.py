# Calcular e exibir a média ponderada de três notas (pesos 2, 3 e 5).
a = float(input("Digite a primeira nota com peso 2: "))
b = float(input("Digite a segunda nota com peso 3: "))
c = float(input("Digite a terceira nota com 5: "))

a=  a*0.2
b = b*0.3
c = c*0.5

media = (a+b+c)

print(f"A média das três notas é {media}")
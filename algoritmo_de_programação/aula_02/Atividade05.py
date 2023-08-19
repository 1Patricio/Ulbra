# Consumo de Combustível - Solicite ao usuário a distância percorrida e a quantidade de combustível usado. Calcule o consumo médio usando Consumo = Distância / Combustível. Mostre o consumo em km/l.
distancia = float(input("Digite a distância do automóvel percorrida em KM"))
combustivel = float (input("Digite a quantidade de combutível usado em Litros"))
consumo = distancia/combustivel
print(f"o consumo do automóvel é de {consumo}Km/L")
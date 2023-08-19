# Conversor de Unidades de Medida - Peça ao usuário uma distância em metros. Converta essa distância para centímetros milímetros. Apresente ambos os valores convertidos.
metro = float(input("Valor da distância em metros"))
centimetros = metro * 100
milimetros = metro * 1000
print(f"A distância de {metro}m em centímetros fica convertido em {centimetros}cm e {milimetros}mm")
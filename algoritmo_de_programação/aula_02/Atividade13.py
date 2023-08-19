# Energia Cinética - Peça ao usuário a massa de um objeto em quilogramas e sua velocidade em metros por segundo. Calcule a energia cinética. Apresente o valor.
massa = float(input("Digite a massa de um objeto em Kg "))
velocidade = float(input("Digite a velocidade do objeto em m/s "))
energia = (massa*(velocidade*velocidade))/2

print(f"A energia cinética do objeto é de {energia}J")
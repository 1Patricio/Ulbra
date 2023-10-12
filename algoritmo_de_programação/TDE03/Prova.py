numAstronautas = int(input("Número de astronautas na missão: "))
diasMissao = float(input("Duração total da missão em dia: "))
consumoOxigenio = float(input("Consumo diário médio de oxigênio por astronauta em litros: "))
consumoAgua = float(input("Coonsumo diário médio de água por astronauta em litros:"))
consumoComida = float(input("Consumo diário médio de comida por astronauta em quilogramas"))
pesoFoguete = float(input("Peso do foguete vazio em quilogramas: "))
eficienciaCombustivel = float(input("Eficiência do combustível (quantos quilometros por litro)"))
distanciaLua = 384400
reservaEmergencia = float(input("Porcentagem de suprimentos extras para emergências: "))
capacidadeTanque = float (input("Capacidade máxima do tanuqe de combústivel em litros: ")) 

supOxigenio = numAstronautas * diasMissao * consumoOxigenio * (1+reservaEmergencia/100)
supAgua = numAstronautas * diasMissao * consumoAgua * (1+reservaEmergencia)
supComida = numAstronautas * diasMissao * consumoComida * (1+reservaEmergencia/100)
combustivel = 2*distanciaLua / eficienciaCombustivel

print(f"Total de oxigênio é {supOxigenio}L, água é {supAgua}L, comida{supComida}Kg")

if combustivel>capacidadeTanque:
    print(f"A quantidade de {combustivel}L de combustível é maior do que a capacidade de {capacidadeTanque}L do tanque")
else:
    print("Tudo certo com a capacidade máxima do tanque do combustível")

supPeso = supOxigenio + supAgua + supComida
excesso = pesoFoguete + (pesoFoguete*0.1)

if supPeso>excesso:
    print("Peso limite dos suprimentos excedeu")
else:
    print("Peso dos suprimentos está dentro dos limites")
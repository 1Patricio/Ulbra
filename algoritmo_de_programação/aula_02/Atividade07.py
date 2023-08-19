# Dias, Horas e Minutos - Solicite ao usuário uma quantidade de minutos. Converta essa quantidade para dias, horas e minutos, considerando que um dia tem 24 horas e uma hora tem 60 minutos. Mostre o resultado da conversão.
minuto = float(input("digite uma quantidade de minutos"))
hora = minuto / 60
dia = hora / 24
print(f"A conversão de {minuto}min são de {hora}h e de {dia}d")
# Rendimento de Juros Simples - Peça ao usuário um valor principal, a taxa de juros e o tempo em anos. Calcule o juro simples. Mostre o valor de juros.
valor = float(input("Digite o valor pricipal R$"))
taxa = float(input("Digite o valor da taxa de juros em porcentagem ao mês "))
tempo = float(input("Digite o tempo de redimento em meses "))

rendimento = (taxa/100)*valor*tempo
montante = valor+rendimento
print(f"O rendimento de Juros Simples fica no valor de R${rendimento} resultando no montante de R${montante}")
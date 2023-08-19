# Rendimento de Poupança - Solicite ao usuário um valor depositado na poupança. Calcule o valor após um mês, considerando uma taxa de rendimento fixa. Mostre o valor atualizado.
deposito = float(input("Digite um valor a ser depositado"))
taxa = float (input("Digite a taxa mensal em %"))
rendimento = taxa/100
valor = deposito + (rendimento*deposito)
print (f"O valor atualizado de R${deposito} com a taxa de {taxa}% é de R${valor}")
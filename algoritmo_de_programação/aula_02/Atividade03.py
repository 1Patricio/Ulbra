# Percentual de Desconto - Peça ao usuário o preço original de um produto e um desconto em porcentagem. Calcule o valor com desconto usando ValorComDesconto = ValorOriginal - (ValorOriginal * Desconto / 100). Mostre o valor após o desconto.
valor_original = float (input("Digite o valor do produto"))
desconto = float (input("Digite o valor do desconto em %"))

valor_desconto = valor_original-(valor_original*(desconto/100))
retirado = valor_original - valor_desconto
print(f"O valor com desconto do produto é de R${valor_desconto} onde foi aplicado um desconto de R${retirado}")
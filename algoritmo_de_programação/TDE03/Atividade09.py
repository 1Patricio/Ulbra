# Calcular e exibir a área de um círculo ou de um retângulo (base e altura fornecidas).

pergunta1 = input("Deseja saber a área de um círculo? (Sim ou Não) ").lower()
if pergunta1 == "sim" or pergunta1 == "s":
    raio = float(input("Digite o raio do círculo em cm: "))
    circulo = 3.14 * (raio * raio)
    print(f"A área do círculo é {circulo} cm²")
else:
    pergunta2 = input("Deseja saber a área de um retângulo? (Sim ou Não) ").lower()

    if pergunta2 == "sim" or pergunta2 == "s":
        base = float(input("Digite a base do retângulo em cm: "))
        altura = float(input("Digite a altura do retângulo em cm: "))
        retangulo = base * altura
        print(f"A área do retângulo é {retangulo} cm²")
    else:
        print("Opção inválida. Volte quando precisar.")
# Verificar se um caractere é uma vogal ou uma consoante.
letra = input("Digite um caractere: ")

letra.lower() #Faz com que as letras fiquem minúsculas 

if letra in "aeiou":
    print("Este caractere é uma vogal")
else:
    print("Este caractere é uma consoante")
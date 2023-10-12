# Escrever um programa que lê as 3 notas obtidas por ele em provas. Para cada aluno, calcular a média de aproveitamento, usando a fórmula:
nota1 = float(input("Digite primeira nota: "))
nota2= float(input("Digite segunda nota: "))
nota3 = float(input("Digite terceira nota: "))

media = (nota1+nota2+nota3)/3

if media >= 9.0:
    print(f"As notas {nota1}, {nota2} e {nota3}, fazem a média {media:.2f} com conceito A sendo aluno APROVADO")
elif media < 9.0 and media >= 7.5:
    print(f"As notas {nota1}, {nota2} e {nota3}, fazem a média {media:.2f} com conceito B sendo aluno APROVADO")
elif media <7.5 and media >= 6.0:
    print(f"As notas {nota1}, {nota2} e {nota3}, fazem a média {media:.2f} com conceito C sendo aluno APROVADO")
elif media <6.0 and media >= 4.0:
    print(f"As notas {nota1}, {nota2} e {nota3}, fazem a média {media:.2f} com conceito D sendo aluno REPROVADO")
else:
    print(f"As notas {nota1}, {nota2} e {nota3}, fazem a média {media:.2f} com conceito E sendo aluno REPROVADO")
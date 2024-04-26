# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

nota1 = int(input('primeira nota:'))
nota2 = int(input('segunda nota:'))

media = (nota1 + nota2)/2

print('sua media é igual a {}'.format(media))

if media < 50:
    print('Média abaixo de 5.0: REPROVADO')
elif media >=50 and media < 70:
    print('Média entre 5.0 e 6.9: RECUPERAÇÃO')
else:
    print('Média 7.0 ou superior: APROVADO')
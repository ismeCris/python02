#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

n1 = int(input('digite o primeiro valor'))
n2 = int(input('digite o segundo valor'))

if n1 > n2:
    print('o primeiro valor e maior')
elif n2 > n1:
    print('o segundo valor e maior')
else:
    print('Não existe valor maior, os dois são iguais')

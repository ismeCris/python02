#: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#: IMC abaixo de 18,5: Abaixo do Peso
#: Entre 18,5 e 25: Peso Ideal
#: 25 até 30: Sobrepeso
#: 30 até 40: Obesidade
#: Acima de 40: Obesidade Mórbida

peso = float(input('qual seu peso:'))
altura = float(input('qual sua altura:'))

imc= peso/(altura * altura)
# imc = peso/(altura ** 2)

print('seu IMC e {:.1f}'.format(imc))

if imc < 18.5:
    print('Abaixo do Peso')
elif imc > 18.5 and peso < 25:
    print('Peso Ideal')
elif imc > 25 and peso < 30:
    print('Sobrepeso')
elif imc > 30 and peso < 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade Mórbida')
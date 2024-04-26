#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER
from datetime import date
atual = date.today().year

nasc = int(input('ano de nascimento: '))
idade = atual - nasc

print('o atleta tem {} anos'.format(nasc, idade))

if idade <= 9:
    print("categoria MIRIM")
elif  idade >9 and idade <= 14:
    print('categoria INFANTIL')
elif  idade >14 and idade <= 19:
    print('categoria JÚNIOR')
elif  idade >19 and idade <= 25:
    print('categoria SÊNIOR')
else:
    print('categoria MASTER')
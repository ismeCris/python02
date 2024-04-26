#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
#se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
atual = date.today().year

nasc = int(input('ano de nascimento:'))
genero = int(input('''qual seu gerero?
            1-mulher
            2-homen
            2004
            '''))

idade = atual - nasc 

print('Quem nasceu em {} tem {} anos em {}.'.format(nasc,idade,atual))
if genero == 1:
    print('Você não precisa se alistar.')

elif idade == 18:
    print('voce tem que se alistar imediatamente.')

elif idade < 18:
    saldo = 18 - idade
    print('ainda faltam {}  anos para o seu alistameto.'.format(saldo))
    ano = atual + saldo
    print('seu alistamento sera em {}'.format(ano))

elif idade > 18: 
    saldo = idade - 18
    print('voce ja devia ter se alistado ha {} anos.'.format(saldo))
    ano = atual - saldo
    print('seu alistamento foi em {}'.format(ano))
2004

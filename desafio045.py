#programa que faça o computador jogar Jokenpô com você.
from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)

print(''' suas opções
    [0] pedra
    [1] pepel
    [2] tesoura''')
jogada = int(input('qual sua jogada? '))
print('-=' *15)
print('computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogada]))
print('-=' *15)

if computador == 0:
    if jogada == 0:
        print('empate')
    elif jogada == 1:
        print('jogador vence')
    elif jogada == 2:
        print('computador vence')
    else:
        ('jogada invalida')

elif computador == 1:
    if jogada == 0:
        print('computador vence')
    elif jogada == 1:
        print('empate')
    elif jogada == 2:
        print('jogador vence')
    else:
        ('jogada invalida')

elif computador == 2:
    if jogada == 0:
        print('jogador vence')
    elif jogada == 1:
        print('computador vence')
    elif jogada == 2:
        print('empate')
    else:
        ('jogada invalida')

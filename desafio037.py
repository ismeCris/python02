#programa que leia um numero qualquer e peça para o usuario escolher qual sera a base da conversão
#1 para binario
#2 para octal
#3 para hexadecimal
num = int(input('digite um numero inteiro:'))
print('''escolha uma base para conversão:
    [1]converter para BINARIO
    [2]converter para OCTAL
    [3]converter para HEXADECIMAL''')

opcao =int(input('sua opção:'))

if opcao ==1:
    print('{}convertido para BINARIO e igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL e igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL e igual a {}'.format(num, hex(num)[2:]))
else:
    print('opção invalida')
    
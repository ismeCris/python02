nome = str(input('qual seu nome?'))
if nome == 'gustavo':
    print('que nome bonito!')
elif nome == 'pedro'or nome=='maria' or nome == 'paula':
    print('seu nome  bem popular no brasil')
elif nome in 'ana claudia jessica juliana':
    print('belo nome')
else:
    print('seu nome e bem normal.')
print('tenha um bom dia, {}!'.format(nome))
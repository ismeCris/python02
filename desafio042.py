print('-='*20)
print('analisador de triangulo')
print('-='*20)

r1=float(input('primeiro seguimento:'))
r2=float(input('segundo seguimento:'))
r3=float(input('terceiro seguimento:'))

if r1 < r2 + r3 and r2 < r1 +r3 and r3 <r1 +r2 :
    print('os seguimentos acima podem formar um triangulo ', end ='')
    if r1 == r2 ==r3:
        print('equilatero')
    elif r1!= r2 != r3 != r1:
        print('escaleno')
    else:
        print('isosceles')
else:
    print('os seguimentos acima nao podem formar triangulo')

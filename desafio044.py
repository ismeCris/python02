#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

print('======== Lojas Cristina ========')
preco=float(input('preço das compras: R$'))

print('''FORMAS DE PAGAMENTO
    [1] á vista dinheiro/cheque
    [2] á vista cartão
    [3] 2x ou mais no cartão
    [4] 3x ou mais no cartão
    ''')
opcao = int(input('qual sua opção? '))

if opcao == 1:
    desconto = preco * (10/100)
    final = preco - desconto
    
    print('sua compra de R${:.2f} vai ficar R${:.2f} no final'.format(preco, final))
elif opcao == 2:
    desconto = preco * (5/100)
    final = preco - desconto
    print('sua compra de R${:.2f} vai ficar R${:.2f} no final'.format(preco, final))
elif opcao == 3:
    print('sua compra  vai ficar R${:.2f} '.format(preco))
elif opcao == 4:
    parcelas = int(input('quantas parcelas?'))
    juros = preco * (20/100)
    final= preco + juros
    mensal = final / parcelas
    print('sua compra sera parcelada em R${:.2f} de R${:.2f} com juros'.format(parcelas, mensal))
    print('sua compra de R${:.2f} vai ficar R${:.2f} no final'.format(preco, final))
else:
    print('opção invalida')
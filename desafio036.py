# programa para aprovar o emprestimo bancario para a compra de uma casa
# o programa deve perguntar o valor da casa, salario e em quantos anos vai pagar
#calcule o valor da prestacao mensal sabendo que nao pode exeder 30% do salario 

casa = float(input('qual o valor da casa: R$'))
salario = float(input('valor do salario: R$'))
anos = int(input('quantos anos de financiamento: R$'))

prestacao =casa / (anos * 12)
minimo = salario * 30 / 100
if prestacao <= minimo:
    print('emprestimo pode ser concedido')
else:
    print('emprestimo negado!')

print('para pagar uma casa de R${:.2f} em {} anos a prestação sera de R${:.2f}'.format(casa, anos, prestacao))
print('comparando tem que pagar {} e o minimo e de {}'.format(prestacao,minimo))
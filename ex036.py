#aprovando um emprestimo
casa = (float(input('Por favor, inserir o valor do ímovel: R$ ')))
salario = (float(input('Informe o sálario do cliente: ')))
anos = int(input('Informe os anos de financiamento: '))
prestacao = casa / (anos * 12)
print('Para pagar o financiamento do ímovel de R$ {:.2f} em anos {}!'.format(casa, anos))
print('A prestação será R$ {:.2f}'.format(prestacao))

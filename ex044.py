#Elabore um programa que calcule o valor a ser pago por um produto
#Considerando o seu preço normal e condição de pagamento
#À vista / dinheiro = 10% de desconto
#À vista no cartão = 5% de desconto
#3x ou mais no cartão: 20% de acréscimo
#Em até 2x no cartão: Preço normal

print('LOJINHA PYTHON')
preco = float(input('Preço das compras:R$ '))
print('''Qual a forma de pagamento:
[ 1 ] Á vista no dinheiro ou pix
[ 2 ] Á vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Escolha a forma de pagamento: ''')
opcao = int(input('Qual a opção de pagamento: '))
if opcao == 1:
    total = preco - (preco * 0.10)
elif opcao == 2:
    total = preco - (preco * 0.05)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra vai ser parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 0.20)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc, parcela))
else:
    total = preco
    print('OPÇÃO INVÁLIDA DE PAGAMENTO, tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(preco,total))

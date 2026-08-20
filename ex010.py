#ex010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar (considere 1USD = R$3,27)
n=float(input('Conversor de R$ em USD > Quantos reais você quer converter? R$'))
dol=n/3.27
print('Com R${} você pode comprar USD {:.2f}'.format(n,dol))

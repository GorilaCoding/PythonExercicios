#ex013 - Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 15% de aumento
print('Gerenciador de aumento de preços')
preco=float(input('Digite o preço do produto: R$'))
aumento=preco*0.15
novop=preco+aumento
print('O produto que custava R${:.2f}, com 15% de aumento, passa a custar R${:.2f}'.format(preco,novop))


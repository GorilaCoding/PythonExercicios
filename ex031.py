#Desenvolva um programa que pergunte a distância de uma viagem em KM
#Calcule o preço da passagem cobrando R$0.50 por KM por viagens até 200km
#e R$0.45 para viagens mais longas

dist = float(input('Qual distância total da viagem: '))
min_dist = 0.50 * dist
max_dist = 0.45 * dist
if dist <= 200:
    print('O valor da passagem é de R${:.2f} reais.'.format(min_dist))
else:
    print('O valor da passagem é de R${:.2f} reais.'.format(max_dist))

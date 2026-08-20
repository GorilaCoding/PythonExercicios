#ex015 - Escreva um programa que pergunte a quantidade de KM rodados por um carro alugado e a quantidade dias pelos
#quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por KM rodado

km = float(input('Quantos KM foram rodados?'))
dias = int(input('Quantos dias o carro foi alugado?'))
preco = (dias * 60) + (km * 0.15)
print ('O valor total a pagar é de R${:.2f}'.format(preco))

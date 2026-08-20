#ex011 - Faça uma programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la. Sabendo que cada litro de tinta pinta 2metros quadrados
print('Vamos calcular a quantidade de tinta necessária para pintar uma parede.')
largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros:'))
area = largura*altura
tinta = area/2
print('A área da parede é de {:.2f} metros quadrados e a quantidade de tinta necessária é de {:.2f} litros.'.format(area, tinta))


#Escreva um programa que leia a velocidade de um carro
#Se ele ultrapassar 80km/h mostre uma mensagem dizendo que foi multado
#A multa vai custar R$7.00 para cada KM acima do limite

vel_carro = float(input('Qual a velocidade do carro? '))
multa = (vel_carro - 80) * 7
if vel_carro >80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('O valor da multa é de R${:.2f}'.format(multa))
else:
    print('Nenhuma multa foi aplicada, tenha um bom dia!')

#Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5
#Peça para o usuário tentar descobrir qual foi número escolhido
#O programa deverá escrever na tela se o usuário venceu ou perdeu

import random
print('Jogo de adivinhação: Tente adivinhar um número entre 1 e 5')
num_int = random.randint(1,5)
num_usu = int(input('Escolha um número entre 1 e 5: '))
if num_usu == num_int:
    print('Você acertou! Parabéns!')
else:
    print('Que pena, você errou, tente novamente!')
print('FIM do jogo')

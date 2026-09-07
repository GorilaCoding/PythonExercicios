#Escreva um programa que leia dois números inteiros e compare-os
#Mostre na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

a = int(input('Escolha um número inteiro: '))
b = int(input('Escolha outro número inteiro '))
if a > b:
    print('O primeiro número é maior: {} > {}'.format(a, b))
elif b > a:
    print('O segundo número é maior: {} > {}'.format(b, a))
else:
    print('Não existe número maior, os dois são iguais: {} = {}'.format(a, b))
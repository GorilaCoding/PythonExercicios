#ex005 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
n=int(input('Digite um número: '))
ante=n-1
suc=n+1
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}.'.format(n,ante,suc))
#ex016 - Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção intera exemplo: digite um número: 6.12752 (parte inteira é 6)
import math
n = float(input('Digite um número real: '))
inteiro = math.trunc(n)
print('O número digitado {} é representado pela parte inteira {}'.format(n, inteiro))


#Escreva um programa que leia um número inteiro qualquer e peça para o usuário
#escolher qual será a base de conversão
#1 para binário
#2 para octal
#3 para hexadecimal
#Quando o usuário escolher alguma das opções o programa vai converter o número para esse tipo

n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opção = int(input('Sua opção '))
if opção == 1:
    print('{} convertido em binário é {}'.format(n, bin(n)[2:]))
elif opção == 2:
    print('{} convertido em octal é {}'.format(n, oct(n)[2:]))
elif opção == 3:
    print('{} convertido em hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida, por favor escolha entre as opções 1, 2 ou 3')


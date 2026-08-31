#Desenvolva um programa que leia o comprimento de três retas e diga
#ao usuário se elas podem ou não formar um triângulo
## PRINCIPIO MATEMÁTICO DA FORMAÇÃO DE UM TRIÂNGULO COM 3 RETAS

a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    print('As retas podem formar um triângulo!')
else:
    print('As retas não podem formar um triângulo!')
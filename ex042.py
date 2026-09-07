#Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo será formado:
#Equilátero: Todos os lados iguais
#Isósceles: Dois lados iguais
#Escaleno: Todos os lados diferentes

a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    print('As retas podem formar um triângulo ', end='')
    if a == b == c:
        print('Equilátero!')
    elif a != b != c !=a:
        print('Escaleno!')
    else:
        print('Isósceles')
else:
    print('As retas não podem formar um triângulo!')
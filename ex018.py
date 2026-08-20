#ex018 - Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente
import math
an  = int(input('Digite um angulo: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O angulo {:.0f} tem o SENO {:.2f}'.format(an, sen))
print('O angulo {:.0f} tem o COSSENO {:.2f}'.format(an, cos))
print('O angulo {:.0f} tem a TANGENTE {:.2f}'.format(an, tan))



#ex017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo e mostre o comprimento da hipotenusa
import math
catad = float(input('Digite o cateto adjacente: '))
catop = float(input('Digite o cateto oposto: '))
hipo = math.hypot(catad, catop)
print('Considerando o cateto adjacente {} e o oposto {}. A hipotenusa vale {:.2f}'.format(catad, catop, hipo))



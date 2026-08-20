#ex014 - Escreva um programa que converta uma temperatura digitada em Celcius para Fahrenheit

c=float(input('Digite uma temperatura em Celsius:'))
f=(c*1.8)+32
print('A temperatura de {:.1f}°C corresponde a {:.1f}°F'.format(c,f))

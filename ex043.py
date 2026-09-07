#Desenvolva uma lógica de que leia o peso e a altura de uma pessoa, calcule seu IMC
#e mostre o seu status de acordo com a tabela abaixo:
#Abaixo de 18.5 = Abaixo do peso
#Entre 18.5 e 25: Peso ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade mórbida

#Meça seu peso em quilos
#Meça sua altura em metros
#Multiplique a altura por ela mesma
#Divida o peso pelo resultado da altura ao quadrado

peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura ** 2)

if imc <= 18.5 and imc <=25:
    print('Seu IMC é {:.0f}, você está no peso ideal!'.format(imc))
elif 25 > imc <= 30:
    print('Seu IMC é {:.0f}, você está com sobrepeso!'.format(imc))
elif imc > 30 and imc >= 40:
    print('Seu IMC é {:.0f}, você está com obesidade!'.format(imc))
else:
    print('Seu IMC é {:.0f}, você está com obesidade mórbida!'.format(imc))
#Faça um programa que leia o ano de nascimento de um atleta e mostre a sua categoria de acordo com a idade:
#Até 9 anos = Mirim
#Até 14 anos = Infantil
#Até 19 anos = Junior
#Até 20 anos = Senior
#Acima de 20 anos = Master

import datetime
ano_atual = datetime.date.today().year
ano = int(input('Digite o ano do seu nascimento: '))
idade = ano_atual - ano
if idade <= 9:
    print('Você tem {} anos de idade, sua categoria é a Mirim.'.format(idade))
elif idade <= 14:
    print('Você tem {} anos de idade, sua categoria é a Infantil.'.format(idade))
elif idade <= 19:
    print('Você tem {} anos de idade, sua categoria é a Junior'.format(idade))
elif idade <= 20:
    print('Você tem {} anos de idade, sua categoria é a Senior.'.format(idade))
else:
    print('Você tem {} anos de idade, sua categoria é a Master.'.format(idade))

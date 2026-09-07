#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade
#Se ele ainda vai se alistar no serviço militar
#Se é a hora de se alistas
#Se já passou do tempo do alistamento
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

import datetime
ano_atual = datetime.date.today().year
ano = int(input('Digite o ano do seu nascimento: '))
idade = ano_atual - ano
if idade < 18:
    print('Ainda não completou 18 anos, faltam {} anos para o alistamento'.format(18 - idade))
elif idade == 18:
    print('Este ano completou/completará 18 anos, está na hora de se alistar!')
elif idade > 18:
    print('Já passou do prazo de alistamento, você está {} anos atrasado, procure uma junta militar!'.format(idade - 18))


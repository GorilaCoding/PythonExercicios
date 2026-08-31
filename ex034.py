#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
#Para salários superiores a R$1.250,00, calcule um aumento de 10%
#Para salários inferiores ou iguais, aumento é de 15%

salario = float(input('Qual o valor do seu salário:R$ '))
sup = salario * 1.10
inf = salario * 1.15
if salario >1250.00:
    print('Seu aumento foi de 10% e seu novo salário é R${:.2f}'.format(sup))
else:
    print('Seu aumento foi de 15% e seu novo salário é R${:.2f}'.format(inf))
#Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
#Calcule o valor da prestação mensal, que vai ser negado se passar de 30% do salário

print('SIMULADOR DE EMPRÉSTIMO BANCÁRIO!')
casa = float(input('Qual o valor da casa a ser adquirida? R$ '))
salario = float(input('Qual o valor do seu salário bruto? R$ '))
prazo = int(input('Em quantos anos a casa será parcelada? '))
prestacao = casa / (prazo * 12)
prazomes = prazo * 12
print('O valor da casa é de R${:.2f}, o prazo de pagamento é de {} meses e o valor da prestação é de R${:.2f}'.format(casa, prazomes, prestacao))
if prestacao > salario * 30 / 100:
    print('Empréstimo Negado! Salário incompatível.')
else:
    print('Empréstimo Aprovado!')
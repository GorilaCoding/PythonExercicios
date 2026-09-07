#Crie um programa que leia duas notas de um aluno e calcule a sua média
#Mostrando no final segundo a média atingida:
#Abaixo de 5.0 = reprovado // 5.0 a 6.9 = recuperação // 7.0 = aprovado

a = float(input('Digite a primeira nota: '))
b = float(input('Digite a segunda nota: '))
media = (a + b) / 2
if media < 5:
    print('A sua média foi {:.1f}, você está reprovado!'.format(media))
elif media < 7.0:
    print('A sua média foi {:.1f}, você está em recuperação!'.format(media))
elif media >= 7:
    print('A sua média foi {:.1f}, Parabéns, você está aprovado!'.format(media))

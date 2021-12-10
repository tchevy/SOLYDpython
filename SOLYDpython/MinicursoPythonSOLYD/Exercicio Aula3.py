'''
EXERCICIO:
Faça um ptograma que pergunte a idade o peso e a altura
de uma pessoa e decida se ela está apta a ser do Exercito

'''


nome = str(input('Insira seu Nome?: '))
nasc = int(input('Que anos voçê Nasceu? : '))
peso = int(input('Qual seu peso?:'))
altura = float(input('Qual sua altura? :'))
ano_atual = 2021
idade = int(ano_atual)-int(nasc)

if idade >= int('18') and altura >= float('1.60') and peso >= int('70'):
    print('Parabéns', nome,'Voçê está apto a se cadastra no Exercito Brasileiro')

else:
    print(nome,':' 'Voçê não tem os requisitos minimos para ingressar no Exército Brasileiro')

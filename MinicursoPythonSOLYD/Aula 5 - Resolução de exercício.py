'''
EXERCICIO: Faça um programa que leia a quantidade de pessoas que serao convidadeas para uma festa.
Após isso o programa irá perguntar o nome de todas as pessoas e colocar numa lista de convidados
Após isso irá imrimir todos os nomes da lista

'''

print('LISTA DE CONVIDADOS 1.0')
print('################################')

num_convidados = input('Digite o numero de convidados: ')
lista_de_convidados = []
nu = 1
while nu <= int(num_convidados):  # for nu in range(int(numero de convidados))
    nome_do_convidado = input('Digite o nome do convidado: '+ str(nu) +':')
    lista_de_convidados.append(nome_do_convidado )
    nu += 1
#print(lista_de_convidados)
for convidados in lista_de_convidados:
    print(convidados)


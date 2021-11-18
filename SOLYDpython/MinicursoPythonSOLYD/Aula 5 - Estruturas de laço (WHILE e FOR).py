# Aula 5 - Estruturas de laço (WHILE e FOR) Lista é um objeto de coleção
#Exemplo01
'''
nomes = ['Roberto', 'Cecilia', 'Meiriane']
#print(nomes)
#exibindo item expecifico

print(nomes[0]) # mostra o item na posição 0 (no caso é o primeiro item, pois a contagem inicia em 0)
print(nomes[1]) # mostra o item na posição 2 (no caso é o segundo item, pois a contagem inicia em 0)
print(nomes[2]) # mostra o item na posição 3 (no caso é o terceiro item, pois a contagem inicia em 0)

#Exemplo02 - for

for nome in nomes: #o for vai percorrer todos os nomes na lista de nomes e vai mostrar o nome (item)
    print(nome)

   #exemplo 02.1
print('Emplo 02.1')
for x in nomes: #o for vai percorrer todos os nomes na lista de nomes e vai mostrar o nome (item)
    print(x)



trabalhando com renge


numero = range(2)
for n in numero:
  print(n)

for par in range(0,10,2):
    print(par)

for imp in range(1,10,2):
    print(imp)


for colecao in range(3):
    print([colecao],nomes)


nu =range(2)
for colecao in range(len(nomes)): # len retonar tods os itens da lista
    print(nu,nomes[colecao])

for i in range (len(nomes)):
    print(nomes[i])
    nomes.append('OII'), 'append adicona o conteudo entra () a lista'

# Usar for dentro de palavras-string

for r in palavras
    print(r)


palavras = ' seduc trabalho'

r = 0

while r < 10:
    print(' R ainda é menor que 10: ', r)
    r = r + 1
print('Acabou o while: ',r)



## LOOP INFINITO
i=0
while True:
    print('Loop infinito!!!:','===', i)
    i = i + 1
    print(i)
'''


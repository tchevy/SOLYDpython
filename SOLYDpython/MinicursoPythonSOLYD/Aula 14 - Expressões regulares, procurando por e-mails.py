import re
import requests

requisicao = requests.get('http://listadeemailmarketinggratis.blogspot.com/2013/10/lista-1-6857-e-mails.html')
#pesquisa = input('Digite sua pesquisa:')
#pesquisa = input('Digite sua pesquisa:')
#string_de_teste = 'lety_helen@yahoo.com  O gato é bonito Roberto, Rocke'
#print(pesquisa)

#padrao = re.search(pesquisa, string_de_teste) # r = raw string
#padrao = re.findall(pesquisa, string_de_teste)
#padrao = re.findall(r'Ro\w+', string_de_teste)
#padrao = re.findall(r',*\w+', string_de_teste)
#padrao = re.findall(r'Ro\w+', string_de_teste) # r = raw string
#padrao = re.findall(r'[Rob]\w', string_de_teste) # r = raw string

padrao = re.findall(r'[\w\.]+[\w-]+@[\w-]+\.[\w\.-]+', requisicao.text)   #string_de_teste)
#Pesquisar_Email = re.findall(r'Equipe da EEEP Rita Aguiar Barbosa chega à final da Olimpíada de Língua Portuguesa', requisicao.text)   #string_de_teste)


#padrao = re.search ('',string_de_teste) # a quebra de linha funciona

if padrao:
    print(padrao)
    #print(padrao.group(),'.')
    #print(padrao)
else:
    print("Padrão Não Encontrado")

'''
if padrao:
    print(padrao)
    #print(padrao.group(),'.')
    #print(padrao)
else:
    print("Padrão Não Encontrado")

#print("oi pessoal\nSegunda linha")
'''

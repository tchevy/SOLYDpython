import requests
import json

def requisicao(titulo):
     try:
       req = requests.get('http://img.omdbapi.com/?apikey=[3bb7744d]&' + titulo)
       dicionario = json.loads(req.text)
       return dicionario
     except:
       print('Erro na conexão')
       return None

def printar_detalhes(filme):
     print('Título:', filme['Title'])
     print('Ano:', filme['Year'])
     print('Diretor:', filme['Director'])
     print('Atores:', filme['Actors'])
     print('Nota:', filme['imdbRating'])

sair = False
while not sair:
    op = input('Escreva o nome de um filme ou SAIR para fechar:')
    if op == 'SAIR':
        sair = True
        print('Saindo...')
else:
     filme = requisicao(op)
     if filme['Response'] == False:
         print('Filme nao encontrado')
     else:
         printar_detalhes(filme)

#print(req.text)


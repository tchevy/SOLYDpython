import requests
import time

cabecalho = {'Uer-agente': 'Windows 2022',
             'Referer':'https://googgle.com'}
                        #import Beautiful Soup 4 BS4 pip install bs4

meus_cookies = {'Ultima-Visita': '01-12-2021'}
dados = {'username': 'tchevy',
         'password': 'qwe123'}
texto = None
try:
    requisicao = requests.post('https://putsreq.com/jqAHeP8aIP8RFayEpbP1',
                              headers=cabecalho,
                              cookies=meus_cookies,
                              data=dados)
    texto = requisicao.text
except Exception as e:
    print("A requisição deu erro:", e )

print(texto)

'''
    requisicao = requests.get('https://putsreq.com/HWON7wBhaWD4dJ1EP7RZ')
    print(requisicao.text)
    requisicao2 = requests.post('https://www.seduc.ce.gov.br/')
    print(type(requisicao))
    print(type(requisicao2))
    print(requisicao.status_code) # recebe o status da requisção
'''


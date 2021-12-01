import requests

                        #import Beautiful Soup 4 BS4 pip install bs4
texto = None
try:
    requisicao = requests.get('https://putsreq.com/LZKDmO54nggSWu1c302a')
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


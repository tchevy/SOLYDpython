import requests
import json
import time

cidade = input("Escreva sua cidade: " )

requisicao = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+ cidade+'&appid=afa245d7cf327631c96e0cf8dc403a64')
print(requisicao.text)

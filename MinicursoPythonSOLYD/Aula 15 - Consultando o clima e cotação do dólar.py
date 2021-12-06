#COTAÇÂO DO DOLLAR
import requests
import json
#requisicao = requests.get('https://api.hgbrasil.com/finance/stock_price?key=908b0482&symbol=bidi4   908b0482&symbol=bidi4')
#print(requisicao.text)
"""
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=IBM&apikey=VCJF25RNXTCWPFUU'
r = requests.get(url)
data = r.json()
print(data)
"""

requisicao = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=IBM&apikey=VCJF25RNXTCWPFUU')
cotacao = json.loads(requisicao.text)
print(cotacao)

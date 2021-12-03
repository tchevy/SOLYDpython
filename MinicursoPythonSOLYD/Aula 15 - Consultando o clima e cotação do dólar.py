#COTAÇÂO DO DOLLAR
import requests
requisicao = requests.get('https://api.hgbrasil.com/finance/stock_price?key=908b0482&symbol=bidi4   908b0482&symbol=bidi4')
print(requisicao.text)

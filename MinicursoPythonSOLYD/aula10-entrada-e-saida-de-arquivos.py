#arquivo = open('/home/roberto.dias/Lista-de-Palavras.txt','r')
#arquivo = open('/home/roberto.dias/Lista-de-Palavras.txt', 'w')
#arquivo = open('/home/roberto.dias/Lista-de-Palavras.txt','b')
#arquivo = open('/home/roberto.dias/Lista-de-Palavras.txt', 'rb')
#arquivo = open('/home/roberto.dias/Lista-de-Palavras.txt', 'a')
try:
     arquivo2 = open('teste.txt')
     # arquivo = open('/home/roberto.dias/Orçamento-Laiana-Cunha-2021-10-25.pdf', 'rb')
     print(arquivo.read())
except Exception as erro:



     print(erro)


#print() ---> imprime o conteudo na tela
#len() ---> infora a quantidade de caracter, é usado junto com print Ex. print(len("Olá Mundo"))
print(len ("Olá Mundo"))
# Podemos fazer nossas proprias funçoes
# Ex.
def soma(numero1, numero2):
    resp = numero1 + numero2
    return resp
resposta = soma(256, 478)
print(resposta)

def imprime_oi():
    print("OI TUDO BEM?")

imprime_oi()
imprime_oi()
imprime_oi()


def tem_sete_letras(objeto):
    if len(objeto) == 7:
        return True
    else:
        return False
if tem_sete_letras('Roberto'):
    print("Realmente tem sete caracter")
else:
    print("Não tem sete caracter")


'''
EXERCICIO: Escreva uma funçao que receba 
um objeto de coleção e retorna o valor 
do maior numero dentro dessa coleção
'''
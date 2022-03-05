"""
Exercício Saudação
"""
## SAUDAÇÃO
def funcao(msg, nome):
    return f'{msg}, {nome}'

saudacao = 'Olá'
nome = 'Jonas Ferreira'

valor = funcao(msg=saudacao,nome=nome)
print(valor)

# NUMEROS
def funcao_n(n1, n2, n3):
    soma = n1 + n2 + n3
    return soma

n1 = 1
n2 = 2
n3 = 3
valor = funcao_n(n1, n2, n3)
print(valor)

# SOMAS PORCENTUAL
def aumento_percentual(n1, n2):
    result = n1 + (n1 * n2) / 100
    return result

n1 = 100
n2 = 15

valor = aumento_percentual(n1, n2)
print(valor)

# FIZZ BUZZ
def funcao_fb(number):
    resposta = ''
    if number % 3 == 0:
        resposta += 'Fizz'
    if number % 5 == 0:
        resposta += ' Buzz'

    return resposta.strip() if resposta != '' else f'{number} não é divisível por 3 e 5'

# Gerar números aleatórios
from random import randint

for i in range(100):
    aleatorio = randint(0,100)
    resultado = funcao_fb(aleatorio)
    print(resultado)






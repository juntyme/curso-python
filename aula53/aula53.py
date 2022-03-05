"""
Funções (def) em Python - return
"""

def funcao(var):
    return var
    print('Isso não será executado.')

var = 'Valor desejado.'
valor = funcao(var)

# Verifica se é True or False
if valor:
    print(valor) # sem valor retorna "NONE" sem valor
else:
    print('Nenhum valor.')


def divisao(n1, n2):
    if n2 == 0:
        return # retorna NONE

    return n1 / n2

divide = divisao(8,4)

if divide:
    print(divide)
else:
    print('Conta Invalida')


# CHECAR VARIAVEL E FUNÇÃO
def dumb():
    return [1,2,3,4]

# verificar funcão
print(dumb(), type(dumb()))

# Verificar variavel
var = dumb()
print(var, type(var))



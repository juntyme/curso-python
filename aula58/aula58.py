# Duas Funções

def func2(parametro1, parametro2):
    return parametro1, parametro2

def func1(parametro1, parametro2):
    resultado = func2(parametro1, parametro2)
    return f'{resultado[0]} {resultado[1]}'

parametro1 = 'Olá, '
parametro2 = 'Jonas'
print(func1(parametro1, parametro2))


"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada.
"""

def ola_mundo():
    return 'Olá mundo!'


def mestre(funcao):
    return funcao()


print(ola_mundo())

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando = mestre(fala_oi, 'Luiz')
executando2 = mestre(saudacao, 'Luiz', saudacao='Bom dia!')
print(executando)
print(executando2)
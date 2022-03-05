# Variavel de scope global
variavel = 'valor'

def func():
    print(variavel)

func()

# Scope Local
def func2():
    global variavel # Não é recomendado mas pode alterar em modo global não é boa pratica de comportamento
    variavel = 'Outro Valor' # Variavel criada no scope local acessivel apenas a funcão func2
    print(variavel)

func2()

print(variavel)

def func3():
    print(variavel)
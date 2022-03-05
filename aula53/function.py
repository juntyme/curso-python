
"""
Retornar funções em cascatas
"""

def f(var):
    print(var)

def dumb():
    return f

var = dumb()
print(id(var), id(f)) # Checa o ID no

if var == f:
    print('var é igual a f')
else:
    print('não vai ser executado')
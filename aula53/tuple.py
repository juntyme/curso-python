"""
Funções (def) em Python - return
"""
def dumb():
    return 'luiz', 'Otávio' # semelhante ('luiz', 'Otávio') => retorna tuple  !=  => retorna list

var = dumb()

# tuple uma lista que não pode ser alterada
print(var, type(var))
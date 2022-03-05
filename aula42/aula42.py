"""
DESEMPACOTAMENTO
ENUMERATE - Enumerar elementos da lista # list
"""
lista = [
    ['Edu', 'João', 'Luiz'],
    ['Maria', 'Aline', 'Joana'],
    ['Helena', 'Ed', 'Lu'],
]

for v1 in enumerate(lista, 53):  # enumera o elemento e informe o valor inicial.
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista # desempacotamento simples
    print(valor_enumerado)

# Type catch mudar o tipo com dupla em python não pode adicionar e nem remover da lista
enumerada = list(enumerate(lista))
# result
# [(0, ['Edu', 'João', 'Luiz']), (1, ['Maria', 'Aline', 'Joana']), (2, ['Helena', 'Ed', 'Lu'])]
print(enumerada[0][1][2])

# result
# [(0, ['Edu', 'João', 'Luiz']), (1, ['Maria', 'Aline', 'Joana']), (2, ['Helena', 'Ed', 'Lu'])]
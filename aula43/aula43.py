"""
Desempacotamento de lista e python
"""
lista = ['Luiz', 'João', 'maria', 'Jonas']

n1, n2, * outra_lista, penultimo, ultimo = lista  # divide a lista e cria outra variavel lista
n5,n6, *_ = lista

print(penultimo, ultimo)
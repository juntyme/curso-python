"""
Lista em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

texto = 'Valor'
# acessar os valores utilizando os indeces poder ser positivo ou negativo
# uma variavel guarda apenas um valor, a lista guarda vários valores
#          0, 1, 2, 3, 4
# lista = [1, 2, 3, 4, 'Jonas Ferreira', True, 12.00] # tipo array
# #       -  4, 3, 2, 1, 0
#
# lista[6] = 'Alterar o float'  # alterar atributo da lista
#
# print(lista[:6]) # selecinar até o 6
# print(lista[::-1]) # Reverter a lista

# lista1 = [1,2,3]
# lista2 = [4,5,6]
# lista3 = lista1 + lista2  # concatenar listas
#
# lista1.extend(lista2) ## extender a lista2
# lista1.append('a') # adiciona valor no final da lista, insere um valor ao final da lista
# print(lista1)
# lista2.insert(0,'c') # adicina no começo, altera todos os indices
# print(lista2)
# lista1.pop() # retira o último item da lista
#
# del(lista2[2:4]) # deleta os selecionados da lista
#
# print(lista1)
# print(lista2)
# print(lista3)
# print('Verificar min e max')
# print(max(lista1))
# print(min(lista1))

# Converter objeto literaveis de uma lista
lista4 = list(range(1,100, 8))
print(lista4)

soma = 0
for valor in lista4:
    print(valor)
    soma = soma + valor

print(soma)
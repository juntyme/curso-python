"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # Str
* Enumerate - Enumerar Elementos da lista # list / para objetos iteráveis
"""
# FUNÇÃO ENUMERATE
lista_2 = ['Luiz','João','Maria']
for indice, nome in enumerate(lista_2): # desempacotamento
    print(indice, nome)

# exemplo de desempacotamento simples
n1, n2, n3 = lista_2
print(n2)


# string = 'O Brasil é penta'
# lista = string.split(' ')
#
# for indice, valor in enumerate(lista):
#     print(indice, valor, lista[indice])

# FUNÇÃO JOIN
# string = "O Brasil é o país do futebol, o Brasil é penta."
# lista = string.split(' ')
#
# string2 = ' '.join(lista)  # Função Juntar lista
#
# print(string)
# print(lista)
# print(string2)

# FUNÇÃO SPLIT
# string = "O Brasil é o país do futebol, o Brasil é penta."
# lista_1 = string.split(' ')
# lista_2 = string.split(',')
#
# for valor in lista_2:
#     print(valor.strip().capitalize()) # função strip remove os espaços do inicio ao fim

#
# palavra = ''
# contagem = 0
# for valor in lista_1:
#     qtd_vezes = lista_1.count(valor)
#
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor
#
# print(f'A Palavra {palavra} apareceu {contagem} x na frase.')

"""
EXPREÇÕES CONDICIONAIS OR
"""

nome = input('Qual o seu nome? ')

print(nome or 'Voce não digitou nada!') # Verificador conteudo
# pode utilizar print(nome or Nome or outra_coisa or 'Final')

if nome:
    print(nome)
else:
    print('Você não digitou nada =(')

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Luiz'

variavel = a or b or c or d or e or f or g

print(variavel)
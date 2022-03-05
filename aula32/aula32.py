"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:. - (NÚMERO)f - quantidade de casas decimais (float)

> - Esquerda
< - Direita
^- Centro
"""

num_1 = 10
num_2 = 3

divisao = num_1 / num_2

print('{:.3f}'.format(divisao)) # com três casas decimais
print(f'{divisao:.2f}')  # com duas casas decimais

# Trabalhando com string
nome = 'Jonas Ferreira'
print(f'{nome:s}')

# Trabalhando com numeros
num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0>10}')

num_3 = 1150
print(f'{num_3:0^10}')

num_4 = 1150
print(f'{num_4:0<10}')

num_5 = 1150
print(f'{num_5:.2f}')

num_6 = 1150
print(f'{num_6:0>10.2f}')


## Trabalhando com string

nome = 'Otávio MIranda'
print(f'{nome:#^50}')

nome_formatado = '{:@^50}'.format(nome);
print(nome_formatado)

nome_formatado_2 = '{n:@^50}'.format(n=nome);
print(nome_formatado_2)

print(nome.ljust(20, '#'))
print(nome.lower())  # Tudo minusculos
print(nome.upper()) # Tudo maiusculo
print(nome.title()) # Primeiras Letras Maiusculas
print(nome.capitalize())

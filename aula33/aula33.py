"""
Manipulando strings

* String Indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc..
Essas funções podem ser usadas diretamente em cada tipo

Voce pode conferir tudo isso em
https://docs.python.org/3/library/stdtypes.html
https://docs.python.org/3/library/functions.html

"""
# indices positivos  [0123456789]
texto = 'Python s2'
# indices negativos -[9876543210]
print(texto[0])

# retirar por negativo
url = 'www.google.com.br/'
print(url[:-1])

# entre seleções de caracteres
nova_string = texto[0:6]  # texto[:6]
print(nova_string)

# da seleção ao último
nova_string2 = texto[6:]
print(nova_string2)

# Seleção pelo negativo
nova_string3 = texto[-9:-3]
print(nova_string3)

# Seleção com pulos de caracteres
nova_string4 = texto[0:6:2]
print(nova_string4)
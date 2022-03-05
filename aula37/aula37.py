"""
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
"""

texto = 'Python'

# c = 0  # contador
# while c < len(texto):
#     print(texto[c])
#     c += 1

# enumera o laço
for n, letra in enumerate(texto):
    print(n, letra)

# Função range recebe três argumentos range(start=0, stop, step=1)
# decrementa  range(20, 10, -1)
# pula número range(0, 10, 2)
for numero in range(0, 100, 8):
    print(numero)

print('##########')

## É um contador
for n in range(100):
    if n % 8 == 0: # Modulo de divisão
        print(n)

# continue - pula pra o proximo laço
# break - termina o laço

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)
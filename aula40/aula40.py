"""
Fro / Else em python
"""
# continue
# break

variavel = ['Luiz Oávio', 'Joãozinho', 'Maria']


for valor in variavel:

    if valor.lower().startswith('j'):
        break
        # continue
        # break
    print(valor)
else:
    print('Não existe uma palavra que começa com J')

"""
Condições IF, ELIF e ELSE
if => se
else => ou
elif=> se for isso
"""

if False:
    print("É Verdadeiro.")
elif False:
    print("Agora Verdadeiro")
elif True:
    print("Mais um Verdadeiro")
    nome = input("Qual o seu nome? ")

    print(f'Seu nome e {nome}.')
else:
    print("Não é verdadeiro")

print('A Minha expressão não é verdadeira')
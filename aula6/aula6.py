"""
Iníciar com letra, pode conter números, separar _, letras minúsculas
linguagem de tipagem dinâmica
"""

nome = 'Jonas Ferreira'  # str
idade = 40  # int
altura = 1.72 # float
e_maior = idade > 18  # Expressão  True ou False
peso = 76  # int
imc = peso / (altura ** 2)

print('Nome:', nome)
print('Idade:', idade)
print('Altura',  altura)
print('É maior:', e_maior)

print(idade * altura)

print(nome, 'tem', idade, 'de idade e seu IMC é', imc)

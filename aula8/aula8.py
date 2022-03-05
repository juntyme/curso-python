nome = 'Jonas Ferreira'
idade = 41
altura = 1.72
e_maior = idade > 18  # Expressão
peso = 76
imc = peso / (altura ** 2)
ano_atual = 2022
nascimento = ano_atual - idade


print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')
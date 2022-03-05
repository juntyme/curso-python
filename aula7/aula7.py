nome = 'Jonas Ferreira' # str
idade = 40  # int
altura = 1.72  # float
e_maior = idade > 18  # Operador Relacional bool
peso = 76 # int
imc = peso / (altura ** 2)  # int / potenciação
ano_atual = 2022  # int
nascimento = ano_atual - idade

print(nome, 'tem', idade, 'de idade e seu IMC é', imc)

# Utilizar F string
print(f'{nome} tem {idade} anos de idade e seu imc e {imc:.2f}')

# Format indice numerico
print('{0} tem {1} anos e seu imc é {2:.2f}'.format(nome, idade, imc))

# Format com nomes nomeados indice nomeados n, i , im
print('{n} tem {i} anos e seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))

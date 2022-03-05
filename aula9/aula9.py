"""
Entrada de dados - Aula9
"""
# Variaveis
nome = input("Qual o seu nome? ")  # sempre vai retornar uma string
idade = input("Qual a sua idade? ")
ano = 2022
ano_nascimento = ano - int(idade)

print(f'O usuário digitou {nome} e o tipo da variável é'
      f' {type(nome)}')

print(f'{nome} idade {idade}.'
      f'{nome} nasceu em {ano_nascimento}.')
""""
Operadores Relacionais
== > >= < <= !=
== igualdade (tipo e valor)
> maior que
>= maior que e igual a
<= menor que e igual a
!= diferente
"""
num_1 = 2  # int
num_2 = 2  # int

expression = (num_1 == num_2)

print(expression)  # Esta perguntando se é iguais resposta bool true or false

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))


# Limite para pegar empréstimo
idade_limite = 18
idade_menor = 20  # muito jovem
idade_maior = 30  # passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar empréstimo')
else:
    print(f'{nome} não pode pegar empréstimo')


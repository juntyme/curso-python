"""
Verificar Erros
"""

num1 = input('Digite um número: ')
num2 = input('Digite um número: ')

#  experimentar
try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('erro')
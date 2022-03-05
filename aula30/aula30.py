"""
Exercicios


"""

numero_inteiro = input('Digite um número inteiro: ')

if numero_inteiro.isdigit():

    numero_inteiro = int(numero_inteiro)

    if numero_inteiro % 2 == 0: # Modulo com resto todo numero par é dividido por 2
        print(f'{numero_inteiro} é Par')  # Funcion string
    else:
        print(f'{numero_inteiro} é Impar') # Funcion String

else:
    print('Não é um número inteiro')

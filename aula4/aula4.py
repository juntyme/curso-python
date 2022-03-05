"""
Tipos de dados
str - str() string - ex: 'Texto'
int - int() inteiro (positivo, negativo ou zero) - ex: 123 , -122
float - float() real/ponto flutuante com ponto (positivo, negativo, zero) ex: 12.00, -12.99, 0.0
bool - bool() booleano/lógico  true (1) / false (0)
"""
print('Jonas', type('Jonas')) ## Chamando uma Classe
print(123, type(123))
print(12.23, type(12.23))
print(10 == 10, type(10 == 10))
print('l' == 'L', type('L' == 'L'))
print(bool('')) # Retorna false
print(bool(0)) # Retorna false
print(bool(0.0)) # Retorna false

# Type catch
print('Jonas', type('Jonas'), bool('luiz'))

# Converter String para int
print('10', type('10'), type(int('10')))

# Exercicios
# Nome
print('Jonas Ferreira', type('Jonas Ferreira'))

# Idade
print(40, type(40))

# Altura
print(1.70, type(1.70))

# Maior de Idade
print(40 > 18, type(40 > 18))
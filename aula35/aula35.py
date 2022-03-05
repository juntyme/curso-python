"""
While / Esle
contadores
acumuladores
"""
contador = 1
acumulador = 1

while contador <= 10: # True or False
    print(contador, acumulador)

    # Para o while
    if contador > 6:
        break

    acumulador = acumulador + contador  # Operações Aritméticas
    contador += 1
else: # while igual a false
    print('Finalizou')

print('Isso será executado')
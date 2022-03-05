""""
Contar Caracteres, não funciona com tipos numéricos
"""
usuario = input("Digite seu usuário: ")
qtd_caracteres = len(usuario)  # Funciton count caracters

if qtd_caracteres < 6:
  print('Você precisa digitar pelo menos 6 caracteres')
else:
 print('Você foi cadastrado no sistema')

print(usuario, qtd_caracteres, type(qtd_caracteres))

string1 = input('Digite alguma coisa: ')
string2 = input('digite outra coisa: ')

print(f'1 A quantidade total de caracteres digitados foi {len(string1) + len(string2)}')
print(f'2 A quantidade total de caracteres digitados foi {string1.__len__() + string2.__len__() }')
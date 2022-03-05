usuario = input('Nome de Usuário: ') # sempre será string
senha = input('Senha do usuário: ')

usuario_db = 'Luiz'
senha_db = '123456'

if usuario_db == usuario and senha_db == senha:
    print('Você esta logado.')
else:
    print('Usuário ou Senha inválido')

nome = 'Otávio Miranda'
idade = 29

if idade > 18:
    print(f'{nome} é adulto.')
else:
    print(f'{nome} NÃO é adulto.')
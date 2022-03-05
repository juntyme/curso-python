"""
Operado ternário em Python
"""
logged_user = True

# msg = 'usuario logado.' if (logged_user == True ) else 'Usuario precisa se logar.'
msg = 'usuario logado.' if logged_user else 'Usuario precisa se logar.'

# if logged_user:
#     msg = "Usuário Logado."
# else:
#     msg = 'Usuario precisa se logar.'

print(msg)

# VERIFICAR IDADE
idade = input('Qual a sua idade: ')

if not idade.isnumeric():
    print('Você precisa digitar apenas números.')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = "Pode acessar" if e_de_maior else 'Não pode acessar.'

    print(msg)

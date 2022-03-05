"""
Funções - def em Python (Part 1)

Repetições utilize Variaveis ou Funções

"""
# Definimos as propria funções com def
# As funções recebe parametros => argumentos
def funcao(_msg = 'Hello, ', _nome='User'):
    _nome = _nome.replace('e', '3') # replece() altera os valores
    return f'{_msg} {_nome}'

msg = 'Olá, '
nome = 'Jonas Ferreira'
v_1 = funcao(msg, nome) ## envio de variavel diretamente
v_2 = funcao() # envio sem variaveis
v_3 = funcao(_nome=nome, _msg=msg) ## Função com valores nomeados

print(v_3)
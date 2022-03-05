nome = input('Qual é seu nome? ')

tamanho = len(nome)

if tamanho <= 4:
    print('Seu nome é Curto')
elif tamanho <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
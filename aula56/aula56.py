"""
Funções (def) em Python - *args ** kwargs -

"""
# Partir do momento que seta um padrão todos posteriores tem que serguir o padrão
def func(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a1, a2, a3, a4, a5, nome, a6)
    return nome, a6 # retorna uma tuple

var = func(1,2,3,4,5, nome='Luiz')
print(var[0], var[1])


# Numeros de argumentos indefinidos  (*args) pode ser qualquer argumento ex: *tuples
def func_2(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args)) # não pode ser alterado

    args = list(args) # Transforam em lista
    args[0] = 'Jonas' # Altera o atributo da lista
    print(args)


lista = [1,2,3,4,5]
print(lista)
print(*lista, sep='-') # Desempacotando a lista com argumento sep
n1, n2, *n = lista
var = func_2(1,2,3,4,5,6,7,9)

# Junção de tuple
lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
print(*lista,*lista2) # Junção da tuple

# FUNÇÃO *args **kwargs ler kw args
def func_3(*args, **kwargs):
    print(args)
    print(kwargs)
    # print(kwargs['nome'], kwargs['sobrenome'])
    nome = kwargs.get('nome') # não gerar erro se não existe retorna NONE
    print(nome)

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func_3(*lista, *lista2, nome='Luiz', sobrenome='Ferreria')
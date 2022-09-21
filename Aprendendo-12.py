'''
Iniciando em mesma ordem porém vazio:
lista = []
tupla = ()
dicionario = {}
conjunto = set()
'''
minha_lista = ['Gui', 'Joao'] # Vetor / Lista (list)
minha_tupla = ('Gui', 'Joao') # Tupla (tuple), um vetor/array imutável
meu_dicionario = {'nome': 'Guilherme', 'idade': 27} #Dicionário (dict) / Objeto de tipo Json
                  #KEY    #VALUE
meu_conjunto = {'Guilherme', 'Joao'} # Conjunto | não possuí valores iguais e não possui chave

if 'Gui' in minha_tupla:
    print('Gui está na tupla')
else:
    print('Gui não está na tupla')

if 'Guilherme' in meu_dicionario.values():
    print('Guilherme está no dicionário')
else:
    print('Guilherme não está no dicionário')

meu_dicionario['idade'] = 40
meu_dicionario['endereco'] = 'Avenida João das Neves'

print(meu_dicionario)

meu_conjunto.add('Maria')
meu_conjunto.add('Rodrigo')

print(meu_conjunto)

if 'Guilherme' in meu_conjunto:
    print('Guilherme está no conjunto')
else:
    print('Guilherme não está no conjunto')
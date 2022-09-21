'''
Escreva uma função que recebe um objeto de coleção e retorna o valor do maior numero dentro dessa coleção
e outra função que retorne o menor número dentro da coleção informada préviamente.
'''

lista_numerica = [3, 2, 1, 4]

def retorna_maior_numero(var):
    ordenada = sorted(var)
    return ordenada[-1]

def retorna_menor_numero(var):
    ordenada = sorted(var)
    return ordenada[0]


print(retorna_maior_numero(lista_numerica))
print(retorna_menor_numero(lista_numerica))
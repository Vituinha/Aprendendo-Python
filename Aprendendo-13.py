'''
Para definir uma função é necessário utilizar o método def
'''

def soma(numero1, numero2):
    resp = numero1 + numero2
    return resp

def tem_sete_itens(var):
    if len(var) == 7:
        return True
    else:
        return False

print(soma(75, 1289))

retorno = soma(29, 82)
print(retorno)

print(tem_sete_itens('1234567'))
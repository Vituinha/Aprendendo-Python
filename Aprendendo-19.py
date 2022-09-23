'''
Try e catch é necessário para ocasiões onde erros são possíveis de ocorrer por variável passada pelo usuário,
sendo sua função = 
try:
    print('teste')
except:
    print('teste2')
Também sendo possível especificar a exception pelo método abaixo e adicionar o erro transitado para uma variável.
'''
try:
    a = 1200/0
except ZeroDivisionError as erro:
    print('Divisão por zero, não é possível prossegior com a operação: ', erro)


print('Imprimindo pós erro proposital.')
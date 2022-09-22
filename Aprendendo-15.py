import sys
'''
Utilizando de importação de requisições para realizar operações necessárias por meio da biblioteca "SYS"
'''
import sys #Importando biblioteca sys

argumentos = sys.argv #argumentos[1] é o que define qual função será chamada, enquanto argumentos[2]/argumentos[3] são os números definidos

def soma(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

if(argumentos[1] == "soma"):
    resp = soma(float(argumentos[2]), float(argumentos[3]))
elif(argumentos[1] == "sub"):
    resp = sub(float(argumentos[2]), float(argumentos[3]))

print(resp)
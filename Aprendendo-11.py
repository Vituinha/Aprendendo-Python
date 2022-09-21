'''
Faça um programa que leia do usuário 5 nomes através do método WHILE ou FOR, após isso, o programa irá perguntar o nome de todas as pessoas e
alocar em uma lista de convidados, com a lista feita, irá imprimir todos os nomes da lista.
'''

quantidade_convidados = int(input("Digite a quantidade de convidados para a festa: "))
contador = 0
nomes = []

while contador < quantidade_convidados:
    nomes.append(input("Digite seu nome: "))
    print("\n")
    contador += 1

for nome in nomes:
    print(nome, "\n")
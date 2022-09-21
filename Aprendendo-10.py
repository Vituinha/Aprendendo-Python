'''
Função WHILE no python funciona sem a necessidade de um vertor, ao contrário da estrutura for demonstrada anteriormente no "Aprendendo-9.py".
O WHILE se orienta a uma excessão, sendo necessário a incrementação para que seja finalizado.
É possível utilizar and e / ou or para WHILE, determinando assim uma função múltipla para sua finalização
Com o uso da função "Break" é possível forçar a parada da execução de um programa préviamente rodado.
'''

i = 0
repeticao = 0
lista_frutas = ['Maçã', 'Pera', 'Uva', 'Abacaxi', 'Goiaba']

contador = 0

for fruta in lista_frutas:
    contador += 1
print(contador, "\n")

while (i < 10 and True) or repeticao <= 5:
    print("I ainda é menor que 10: ", i)
    i = i + 1
    repeticao += 1
print("I é igual a 10")

while True:
    if contador == 20:
        break
    contador += 5
print("\n", contador)
'''
O funcionamento do FOR em python é determinado por lista de array ou vetores, tendo o primeiro valor como o nome condicional e o segundo como o vetor
ou array determinado com antecedência durante o código.
A função Range cria uma lista com os números deliberados na função com a possibilidade de determinar qual o número inicial como em: range(0, 100) e
ainda acrescentando ao aumentar os passos pelo array com a função completao: range(0, 100, 2).
É possível realizar FOR para uma string comum por conta da mesma ser tratada como um vetor.
'''
nomes = ['Guilherme', 'Marcelo', 'João', 'Júlia']
tamanho_nomes = len(nomes)
palavra = "Texto complexo para impressao"

lista_de_numeros = range(5)

for item in range(tamanho_nomes):
    print(nomes[item])

print("\n")

for i in lista_de_numeros:
    print(i)

print("\n")

for nome in nomes:
    print(nome)

print("\n")

for nome in range(tamanho_nomes):
    nomes.append(nomes[nome])

print(nomes)

print("\n")

for letra in palavra:
    print(letra)
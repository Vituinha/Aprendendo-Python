'''
Formação de um Vetor/Array multidimensional e aceita valores como -1 que se referencia ao último valor do array como: lista[-1]
também é possível selecionar de passos, como em: lista[0:5] (selecionando do primeiro ao quinto elemento) e é possível alterar o passo
como pode ser observado em: lista[0:5:2].
Lembrando que toda string para python é um vetor, assim sendo, é possível selecionar letras separadas na string.
Função lista.split('STRING DE SEPARAÇÃO') irá separar em um novo array com a string determinada.
Para concatenação de string, basta realizar a operação com "+"
'''
lista = ['Joao', 'Maria', 'Guilherme', 'Diego', 10, 10.2, True, ['Matheus', 'Laís', 'Victor']]
lista.append('Roberto')
lista.remove('Joao')
lista.insert(0, 'Rodney')
lista[1] = "Raquel"

contador_guilherme = lista.count('Guilherme')

print(contador_guilherme, len(lista))
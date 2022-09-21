#\t siginifica tab, \n significa nova linha.
print("Hello World!\nNovaLinha\tDistante Por Tab\n\n")
nome = input("Escreva seu nome: ")
idade = input("Escreva sua idade: ")
altura = input("Escreva sua altura: ")

print('Nome:', nome, 'Idade:', idade, 'Altura:', altura)
#outra possibilidade de execução da solução acima, porém com o operador "+"
#print('Nome: ' + nome + ' Idade: ' + str(idade) + ' Altura: ' + str(altura))

print(type(nome), type(idade), type(altura))
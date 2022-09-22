'''
W é o modo de escrita, enquanto R é o modo de leitura enquanto R+ é leitura e escrita e A para apenas adicionar, também existindo
o modo b, utilizado para todos os arquivos com excessão de arquivos de texto.
'''
arquivo = open('Aprendendo Python/Aprendendo-18/arquivo.txt', 'w')

for i in range(0, 1001):
    arquivo.write(str(i) + "\n") # Método write para escrever

arquivo.close

arquivo = open('Aprendendo Python/Aprendendo-18/arquivo.txt', 'r')
for linha in arquivo:
    print(linha)
#print(arquivo.read()) # Método read para leitura
arquivo.close
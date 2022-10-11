'''
Aprendendo sobre API e JSON em python
'''
import requests
import json

def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?t=' + titulo + '&apikey=2d79eeb6')
        dicionario = json.loads(req.text) # Se comporta da mesma forma que um dicionário convencional.
        return dicionario
    except:
        print('Erro na conexao')
        return None

def printar_detalhes(filme):
    print('Titulo:', filme['Title'])
    print('Ano:', filme['Year'])
    print('Diretor:', filme['Director'])
    print('Atores:', filme['Actors'])
    print('Nota:', filme['imdbRating'])
    print('Premios:', filme['Awards'])
    print('Poster:', filme['Poster'])
    print('')


sair = False
while not sair:
    op = input('Escreva o nome de um filme ou SAIR para fechar: ')
    if op == 'SAIR':
        sair = True
        print('Saindo...')
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print('Filme não encontrado, tente novamente')
            print('')
        else:
            printar_detalhes(filme)
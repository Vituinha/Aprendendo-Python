'''
É possível realizar importação de bibliotecas por meio do comando: pip install *nome da biblioteca*,
neste caso foi instalada a biblioteca "requests" para solicitações web.
'''
import requests

cabecalho = {'User-agent': 'windows 12',
             'Referer': 'https://google.com'}

meus_cookies = {'ultima-visita': '10-09-2022'}

dados = {'username': 'guigui',
         'password': '10203040'}

texto = None

try:
    requisicao = requests.post('https://putsreq.com/fjbIWiNmCesjuacFndPb', headers=cabecalho, cookies=meus_cookies, data=dados) 
    # método de realizar requisições é a função requests.get/post/delete/etc... Sendo possível enviar outros dados
    # por meio de virgula e funções como "headers=", "cookies=" e "data="
    texto = requisicao.text
except Exception as e:
    print("A requisição falhou!", e)

print(texto)
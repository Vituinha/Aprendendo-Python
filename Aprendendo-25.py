import oauth2
import json
import urllib.parse

consumer_key = ''
consumer_secret = ''

token_key = ''
token_secret = ''

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token)

query = input("Pesquisa: ")
query_codificada = urllib.parse.quote(query, safe="")

requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q='+query_codificada)
decodificar = requisicao[1].decode()
objeto = json.loads(decodificar)
twittes = objeto['statuses']

try:
    for twit in objeto['statuses']:
        print(twit['user']['screen_name'])
        print(twit['text'])
        print()
except Exception as e:
    print("Ocorreu uma falha: ", e)
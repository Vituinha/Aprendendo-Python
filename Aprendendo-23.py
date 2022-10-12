#API DE COTAÇÃO DE DÓLAR
import requests
import json
import datetime
import time

while True:
    req = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL')
    cotacao = json.loads(req.text)
    print('### COTAÇÃO ###', datetime.datetime.now())
    print(cotacao['USDBRL']['name'], '\nValor em Alta:', cotacao['USDBRL']['high'], '\nValor em Baixa:', cotacao['USDBRL']['low'],'\n\n')
    print(cotacao['EURBRL']['name'], '\nValor em Alta:', cotacao['EURBRL']['high'], '\nValor em Baixa:', cotacao['EURBRL']['low'],'\n\n')
    time.sleep(2)


'''
Expressões Regulares
tendo . como qualquer caracter e \ como caracter de escape, portanto: . = qualquer caracter enquanto \. é apenas o .
\w é qualquer caracter com excessão de espaço vazio sendo possível definir como \w{DIGITO MÍNIMO,DIGITO MÁXIMO} como por exemplo: \w{4,6}
Documentação: https://docs.python.org/3/library/re.html
Site para fazer expressões simples: https://regex101.com/
'''

import re
import requests

site = input('Escreva o site que gostaria de pesquisar por emails: ')

requisicao = requests.get(site)

padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text) # Usar o r para transformar em "RAW STRING"

if padrao:
    print(padrao)
else:
    print('Padrao não encontrado')
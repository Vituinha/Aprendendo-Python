#api de clima/tempo
import requests
import json

input = input("Digite sua Cidade: ")

url = "https://open-weather13.p.rapidapi.com/city/"+input

headers = {
	"X-RapidAPI-Key": "5694604008msh7e6947033578a8fp16458fjsn6e7f44fc4e0f",
	"X-RapidAPI-Host": "open-weather13.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)
req = json.loads(response.text)

print("Coordenadas:", req['coord'], "\n###Dados do Tempo###\nPrincipal:", req['weather'])
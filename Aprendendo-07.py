'''
Faça um programa que pergunte a idade, o peso e a altura de uma pessoa e decide se ela está apta a ser do Exército.
Para entrar no exército é preciso ter mais de 18 anos, pesar mais ou igual a 60 kilos e medir mais ou igual a 1,70 metros.
'''

print("Validação para possível entrada no exército, favor digite sua Idade:\nPeso:\nAltura (em metros):")

idade  = input('Digite sua idade: ')
peso   = input('Digite seu peso: ')
altura = input('Digite sua altura: ')

if idade > '18' and peso >= '60' and altura >= '1.7':
    print("Você está apto a adentrar no serviço militar!")
else:
    if idade <= '18':
        print("Você possui", idade, "anos, portanto, não pode se alistar neste momento!")
    elif peso < '60':
        print("Seu peso atual de", peso, "é menor do que o peso mínimo de 60 Kilos, portanto está impossibilitado de realizar o alistamento!")
    else:
        print("Você mede", altura, "metros, estando abaixo dos 1.70 metros necessários para realizar a inscrição, assim sendo, está inapto ao serviço militar!")
'''
Crie um software de gerenciamento bancário, esse software poderá ser capaz de criar clientes e 
cada cliente possui nome, cpf e idade.
cada conta possui um cliente, saldo, limite (negativo), sacar, depositar e consultar saldo
'''

from clientes import Cliente
from conta import Conta

victor = Conta("Victor", "43186906873", 20, 10, -50)

victor.consulta()
victor.depositar(10)
victor.consulta()
victor.sacar(20)
victor.consulta()
victor.sacar(30)
victor.consulta()
victor.sacar(30)
victor.consulta()
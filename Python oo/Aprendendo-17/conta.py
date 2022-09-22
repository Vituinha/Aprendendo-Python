from clientes import Cliente

class Conta:
    def __init__(self, nome, cpf, idade, saldo, limite):
        Cliente.__init__(self, nome, cpf, idade)
        self.saldo = saldo
        self.limite = limite

    def consulta(self):
        print("Saldo Atual:", self.saldo, "Limite Disponível:", self.saldo - self.limite)

    def sacar(self, saque):
        if self.saldo - saque > self.limite:
            self.saldo -= saque
        else:
            print("Operação inválida, o saque não pode ser concluído por ser maior do que o limite da conta!")

    def depositar(self, deposito):
        self.saldo += deposito

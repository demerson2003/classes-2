# Mantenha este arquivo com a implementação da ContaBancaria
class ContaBancaria:
    def __init__(self, saldo_inicial, cliente):
        self.saldo = saldo_inicial
        self.cliente = cliente

    def depositar(self, valor):
        self.saldo += valor

    def exibir_saldo(self):
        return self.saldo

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")


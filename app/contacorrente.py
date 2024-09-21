from app.contabancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, saldo_inicial, cliente):
        super().__init__(saldo_inicial, cliente)
        self.numero_transacoes = 0

    def depositar(self, valor):
        super().depositar(valor)
        self.numero_transacoes += 1

    def sacar(self, valor):
        if valor <= self.saldo:
            super().sacar(valor)
            self.numero_transacoes += 1


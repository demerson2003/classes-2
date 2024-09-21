# app/contapoupanca.py
from app.contabancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self, saldo_inicial, cliente):
        super().__init__(saldo_inicial, cliente)
        self.saques_mensais = 0
        self.limite_saques = 3

    def sacar(self, valor):
        if self.saques_mensais < self.limite_saques:
            super().sacar(valor)
            self.saques_mensais += 1
        else:
            print("Limite de saques mensais excedido")


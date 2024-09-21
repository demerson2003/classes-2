from .contabancaria import ContaBancaria

class ContaEmpresarial(ContaBancaria):
    def __init__(self, saldo_inicial, cliente, nome_empresa):
        super().__init__(saldo_inicial, cliente)
        self.nome_empresa = nome_empresa

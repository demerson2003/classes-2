class ContaBancaria:
    def __init__(self, saldo_inicial, cliente):
        """Inicializa a conta bancária com um titular e um saldo inicial."""
        self.saldo = saldo_inicial
        self.cliente = cliente

    def depositar(self, valor):
        """Deposita um valor na conta."""
        self.saldo += valor

    def exibir_saldo(self):
        """Exibe o saldo atual da conta."""
        return self.saldo

    def sacar(self, valor):
        """Saca um valor da conta, se houver saldo suficiente."""
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")


class ContaCorrente(ContaBancaria):
    """Classe que representa uma conta corrente com rastreamento de transações."""
    def __init__(self, saldo_inicial, cliente):
        super().__init__(saldo_inicial, cliente)
        self.numero_transacoes = 0

    def depositar(self, valor):
        """Deposita um valor na conta e incrementa o número de transações."""
        super().depositar(valor)
        self.numero_transacoes += 1

    def sacar(self, valor):
        """Saca um valor da conta e incrementa o número de transações."""
        if valor <= self.saldo:
            super().sacar(valor)
            self.numero_transacoes += 1
        else:
            print("Saldo insuficiente")


class ContaPoupanca(ContaBancaria):
    """Classe que representa uma conta poupança com limite de saques mensais."""
    def __init__(self, saldo_inicial, cliente):
        super().__init__(saldo_inicial, cliente)
        self.saques_mensais = 0
        self.limite_saques = 3

    def sacar(self, valor):
        """Saca um valor da conta, respeitando o limite de saques mensais."""
        if self.saques_mensais < self.limite_saques:
            super().sacar(valor)
            self.saques_mensais += 1
        else:
            print("Limite de saques mensais excedido")


class ContaEmpresarial(ContaBancaria):
    """Classe que representa uma conta empresarial com nome da empresa."""
    def __init__(self, saldo_inicial, cliente, nome_empresa):
        super().__init__(saldo_inicial, cliente)
        self.nome_empresa = nome_empresa

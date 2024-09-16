import unittest
from app.cliente import Cliente
from app.contabancaria import ContaCorrente

class TestContaCorrente(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente("Ana Costa", "987.654.321-00")
        self.conta = ContaCorrente(500, self.cliente)

    def test_depositar(self):
        self.conta.depositar(300)
        self.assertEqual(self.conta.exibir_saldo(), 800)

    def test_sacar(self):
        self.conta.sacar(200)
        self.assertEqual(self.conta.exibir_saldo(), 300)

    def test_numero_transacoes(self):
        self.conta.depositar(100)
        self.conta.sacar(50)
        self.assertEqual(self.conta.numero_transacoes, 2)

if __name__ == '__main__':
    unittest.main()
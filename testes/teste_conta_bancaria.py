import unittest
from app.cliente import Cliente
from app.contabancaria import ContaBancaria

class TestContaBancaria(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente("João Silva", "123.456.789-00")
        self.conta = ContaBancaria(1000, self.cliente)

    def test_depositar(self):
        self.conta.depositar(500)
        self.assertEqual(self.conta.exibir_saldo(), 1500)

    def test_sacar(self):
        self.conta.sacar(200)
        self.assertEqual(self.conta.exibir_saldo(), 800)

    def test_sacar_saldo_insuficiente(self):
        self.conta.sacar(1200)
        self.assertEqual(self.conta.exibir_saldo(), 1000)

if __name__ == '__main__':
    unittest.main()

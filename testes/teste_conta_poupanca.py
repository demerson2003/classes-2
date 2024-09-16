import unittest
from app.cliente import Cliente
from app.contabancaria import ContaPoupanca

class TestContaPoupanca(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente("Lucas Pereira", "321.654.987-00")
        self.conta = ContaPoupanca(800, self.cliente)

    def test_sacar(self):
        self.conta.sacar(200)
        self.assertEqual(self.conta.exibir_saldo(), 600)

    def test_sacar_limite(self):
        self.conta.sacar(200)
        self.conta.sacar(200)
        self.conta.sacar(200)
        self.conta.sacar(200)  # Excede o limite
        self.assertEqual(self.conta.exibir_saldo(), 200)

if __name__ == '__main__':
    unittest.main()
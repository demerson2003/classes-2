import unittest
from app.cliente import Cliente
from app.contabancaria import ContaEmpresarial

class TestContaEmpresarial(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente("Empresa ABC", "12.345.678/0001-00")
        self.conta = ContaEmpresarial(1500, self.cliente, "ABC Ltda")

    def test_exibir_saldo(self):
        self.assertEqual(self.conta.exibir_saldo(), 1500)

    def test_nome_empresa(self):
        self.assertEqual(self.conta.nome_empresa, "ABC Ltda")

if __name__ == '__main__':
    unittest.main()

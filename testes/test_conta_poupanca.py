# testes/teste_conta_poupanca.py
from app.cliente import Cliente
from app.contapoupanca import ContaPoupanca

def test_exibir_saldo():
    cli = Cliente("Ricardo Santos", "654.321.987-00")
    conta_poupanca = ContaPoupanca(1000, cli)  # Saldo inicial de 1000
    assert conta_poupanca.exibir_saldo() == 1000

def test_deposito():
    cli = Cliente("Patricia Costa", "321.654.987-00")
    conta_poupanca = ContaPoupanca(1000, cli)
    conta_poupanca.depositar(300)
    assert conta_poupanca.exibir_saldo() == 1300

def test_saque():
    cli = Cliente("Roberto Ferreira", "789.456.123-00")
    conta_poupanca = ContaPoupanca(1000, cli)
    conta_poupanca.sacar(200)
    assert conta_poupanca.exibir_saldo() == 800

def test_limite_saques():
    cli = Cliente("Mariana Rocha", "123.321.654-00")
    conta_poupanca = ContaPoupanca(1000, cli)
    conta_poupanca.sacar(200)
    conta_poupanca.sacar(200)
    conta_poupanca.sacar(200)
    conta_poupanca.sacar(200)  # Excede o limite
    assert conta_poupanca.exibir_saldo() == 400  # Deve permanecer 400


# testes/teste_conta_bancaria.py
from app.cliente import Cliente
from app.contabancaria import ContaBancaria

def test_exibir_saldo():
    cli = Cliente("João Silva", "123.456.789-00")
    conta_bancaria = ContaBancaria(1000, cli)  # Saldo inicial de 1000
    assert conta_bancaria.exibir_saldo() == 1000

def test_deposito():
    cli = Cliente("Ana Maria", "987.654.321-00")
    conta_bancaria = ContaBancaria(1000, cli)
    conta_bancaria.depositar(500)
    assert conta_bancaria.exibir_saldo() == 1500

def test_saque():
    cli = Cliente("Carlos Souza", "456.789.123-00")
    conta_bancaria = ContaBancaria(1000, cli)
    conta_bancaria.sacar(300)
    assert conta_bancaria.exibir_saldo() == 700





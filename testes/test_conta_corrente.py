# testes/teste_conta_corrente.py
from app.cliente import Cliente
from app.contacorrente import ContaCorrente

def test_exibir_saldo():
    cli = Cliente("Marcos Lima", "321.654.987-00")
    conta_corrente = ContaCorrente(1000, cli)  # Saldo inicial de 1000
    assert conta_corrente.exibir_saldo() == 1000

def test_deposito():
    cli = Cliente("Fernanda Silva", "789.123.456-00")
    conta_corrente = ContaCorrente(1000, cli)
    conta_corrente.depositar(200)
    assert conta_corrente.exibir_saldo() == 1200

def test_saque():
    cli = Cliente("Lucia Almeida", "123.789.456-00")
    conta_corrente = ContaCorrente(1000, cli)
    conta_corrente.sacar(500)
    assert conta_corrente.exibir_saldo() == 500

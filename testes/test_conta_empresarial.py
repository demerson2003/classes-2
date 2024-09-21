import pytest
from app.cliente import Cliente
from app.contaempresarial import ContaEmpresarial

def test_exibir_saldo():
    cli = Cliente("Empresa XYZ", "12.345.678/0001-90")
    conta_empresarial = ContaEmpresarial(1000, cli, "XYZ Corp")
    assert conta_empresarial.exibir_saldo() == 1000

def test_deposito():
    cli = Cliente("Empresa XYZ", "12.345.678/0001-90")
    conta_empresarial = ContaEmpresarial(1000, cli, "XYZ Corp")
    conta_empresarial.depositar(200)
    assert conta_empresarial.exibir_saldo() == 1200

def test_saque():
    cli = Cliente("Empresa XYZ", "12.345.678/0001-90")
    conta_empresarial = ContaEmpresarial(1000, cli, "XYZ Corp")
    conta_empresarial.sacar(300)
    assert conta_empresarial.exibir_saldo() == 700



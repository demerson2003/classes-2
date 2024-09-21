# Teste simples das funcionalidades das contas
from cliente import Cliente
from contacorrente import ContaCorrente
from contapoupanca import ContaPoupanca
from contaempresarial import ContaEmpresarial

# Teste Cliente
cli = Cliente("João", "123.456.789-00")
print(f'Cliente: {cli.get_nome()}, CPF: {cli.get_cpf()}')

# Teste Conta Corrente
conta_corrente = ContaCorrente(100, cli)
print(f'Saldo inicial Conta Corrente: {conta_corrente.exibir_saldo()}')
conta_corrente.depositar(50)
conta_corrente.sacar(30)
print(f'Saldo atual Conta Corrente: {conta_corrente.exibir_saldo()}, Transações: {conta_corrente.numero_transacoes}')

# Teste Conta Poupança
conta_poupanca = ContaPoupanca(200, cli)
conta_poupanca.sacar(50)
conta_poupanca.sacar(50)
conta_poupanca.sacar(50)
conta_poupanca.sacar(50)  # Excedendo o limite de saques
print(f'Saldo atual Conta Poupança: {conta_poupanca.exibir_saldo()}')

# Teste Conta Empresarial
conta_empresarial = ContaEmpresarial(1000, cli, "Minha Empresa")
print(f'Conta Empresarial: {conta_empresarial.nome_empresa}, Saldo: {conta_empresarial.exibir_saldo()}')

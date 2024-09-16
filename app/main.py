from cliente import Cliente
from contabancaria import ContaCorrente, ContaPoupanca, ContaEmpresarial

def main():
    print("------------------------------------------")
    cli = Cliente("David Santos", "123.234.456-89")
    print(f'Nome: {cli.get_nome()} -> CPF: {cli.get_cpf()}')

    conta_corrente = ContaCorrente(120, cli)
    print(f'Saldo inicial na Conta Corrente = {conta_corrente.exibir_saldo()}')
    conta_corrente.depositar(50)
    conta_corrente.sacar(30)
    print(f'Saldo após transações = {conta_corrente.exibir_saldo()}')
    print(f'Número de transações = {conta_corrente.numero_transacoes}')

    print("------------------------------------------")
    cli1 = Cliente("Marcos Silva", "987.654.321-00")
    print(f'Nome: {cli1.get_nome()} -> CPF: {cli1.get_cpf()}')

    conta_poupanca = ContaPoupanca(220, cli1)
    print(f'Saldo inicial na Conta Poupança = {conta_poupanca.exibir_saldo()}')
    conta_poupanca.sacar(50)
    conta_poupanca.sacar(50)
    conta_poupanca.sacar(50)
    conta_poupanca.sacar(50)  # Excedendo o limite de saques
    print(f'Saldo após saques = {conta_poupanca.exibir_saldo()}')

    print("------------------------------------------")
    cli2 = Cliente("Empresa XYZ", "12.345.678/0001-90")
    print(f'Nome: {cli2.get_nome()} -> CPF/CNPJ: {cli2.get_cpf()}')

    conta_empresarial = ContaEmpresarial(1000, cli2, "XYZ Corp")
    print(f'Saldo inicial na Conta Empresarial = {conta_empresarial.exibir_saldo()}')
    print(f'Nome da Empresa: {conta_empresarial.nome_empresa}')
    print("------------------------------------------")

if __name__ == '__main__':
    main()

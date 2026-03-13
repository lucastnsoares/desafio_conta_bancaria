from modelos.cliente import PessoaFisica
from modelos.conta import ContaCorrente
from modelos.transacao import Deposito, Saque
import textwrap
from datetime import datetime
from random import randint

def menu():
    menu = """
    === MENU DE OPÇÕES ===

    [1] Nova Pessoa Física
    [2] Nova Conta
    [3] Listar Clientes
    [4] Listar Contas
    [5] Depositar
    [6] Sacar
    [7] Extrato
    [8] Sair

    Digite a opção desejada: """
    return input(textwrap.dedent(menu))

def nova_conta(agencia, contas, clientes):
    cpf = input("\nInforme o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        return (False, "❌ FALHA NA OPERAÇÃO", "Cliente não encontrado! Crie um cliente primeiro antes de criar uma nova conta.")
    
    numero_conta = datetime.now().strftime("%Y%m%d%H%M%S") + str(randint(1000, 9999))
    conta = ContaCorrente(numero_conta, agencia, cliente)
    cliente.adicionar_conta(conta)
    contas.append(conta)
    return (True, "✅ SUCESSO", f"Conta criada com sucesso! Número da conta: {numero_conta}")

def listar_todas_contas(contas):
    if not contas:
        print("\nℹ Nenhuma conta cadastrada!")
        return
    for conta in contas:
        print(conta)

def listar_contas_cliente(cliente):
    if not cliente.contas:
        print("\nℹ Cliente não possui conta cadastrada!")
        return
    for i, conta in enumerate(cliente.contas, start=1):
        print(f"[{i}] Agência: {conta.agencia} | Conta: {conta.numero}")

def listar_clientes(clientes):
    if not clientes:
        print("\nℹ Nenhum cliente cadastrado!")
        return
    for cliente in clientes:
        print(cliente)

def filtrar_cliente(cpf, clientes):
    cliente_filtrado = [cliente for cliente in clientes if cliente.cpf == cpf]
    return cliente_filtrado[0] if cliente_filtrado else None

def selecionar_conta_cliente(clientes):
    """Solicita CPF, filtra o cliente e retorna (cliente, conta_selecionada).
    Retorna (None, None) em caso de falha."""
    cpf = input("\nInforme o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        return None, None
    print("\nContas do cliente:")
    listar_contas_cliente(cliente)
    conta = int(input("\nInforme o número da conta desejada: "))
    if conta > len(cliente.contas) or conta < 1:
        return cliente, None
    return cliente, cliente.contas[conta - 1]

def novo_cliente(clientes):
    cpf = input("\nInforme o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        return (False, "❌ FALHA NA OPERAÇÃO", "Cliente já cadastrado!")
    
    nome = input("Informe o nome do cliente: ")
    data_nascimento = input("Informe a data de nascimento do cliente: ")
    endereco = input("Informe o endereço do cliente: ")
    cliente = PessoaFisica(nome, data_nascimento, cpf, endereco)
    clientes.append(cliente)
    return (True, "✅ SUCESSO", "Cliente cadastrado com sucesso!")

def depositar(contas, clientes):
    cliente, conta_selecionada = selecionar_conta_cliente(clientes)
    if not cliente:
        return (False, "❌ FALHA NA OPERAÇÃO", "Cliente não encontrado!")
    if not conta_selecionada:
        return (False, "❌ FALHA NA OPERAÇÃO", "Escolha inválida!")
    valor = float(input("Informe o valor do depósito: "))
    if valor <= 0:
        return (False, "❌ FALHA NA OPERAÇÃO", "O valor informado para depósito é inválido.")
    transacao = Deposito(valor)
    return cliente.realizar_transacao(conta_selecionada, transacao)

def sacar(contas, clientes):
    cliente, conta_selecionada = selecionar_conta_cliente(clientes)
    if not cliente:
        return (False, "❌ FALHA NA OPERAÇÃO", "Cliente não encontrado!")
    if not conta_selecionada:
        return (False, "❌ FALHA NA OPERAÇÃO", "Escolha inválida!")
    valor = float(input("Informe o valor do saque: "))
    if valor <= 0:
        return (False, "❌ FALHA NA OPERAÇÃO", "O valor informado para saque é inválido.")
    transacao = Saque(valor)
    return cliente.realizar_transacao(conta_selecionada, transacao)
    
def extrato(contas, clientes):
    cliente, conta_selecionada = selecionar_conta_cliente(clientes)
    if not cliente:
        print("❌ Cliente não encontrado!")
        return
    if not conta_selecionada:
        print("❌ Escolha inválida!")
        return
    print("\n" + "=" * 50)
    print("EXTRATO".center(50))
    print("=" * 50)
    print(conta_selecionada.historico)
    print("=" * 50)
    print(f"SALDO DA CONTA: {conta_selecionada.saldo:.2f}")
    print("=" * 50)

def exibir_informacao(titulo, mensagem):
    print("\n" + "="*50)
    print(titulo.center(50))
    print(mensagem)
    print("="*50)

def main():
    sair = False
    agencia = "0001"

    # mock de clientes
    cliente1 = PessoaFisica("Jorge da Silva", "01/01/1990", "11122233344", "Rua A, 123")
    cliente2 = PessoaFisica("Maria Joaquina", "05/05/1985", "55566677788", "Rua B, 456")
    clientes = []
    clientes.append(cliente1)
    clientes.append(cliente2)

    # mock de contas
    conta1 = ContaCorrente("12345", agencia, cliente1)
    conta2 = ContaCorrente("54321", agencia, cliente2)
    conta3 = ContaCorrente("11111", agencia, cliente1)
    conta4 = ContaCorrente("22222", agencia, cliente2)
    contas = []
    contas.append(conta1)
    contas.append(conta2)
    contas.append(conta3)
    contas.append(conta4)   

    cliente1.adicionar_conta(conta1)
    cliente1.adicionar_conta(conta3)
    cliente2.adicionar_conta(conta2)
    cliente2.adicionar_conta(conta4)
    while not sair:
        opcao = menu()
        match opcao:
            case "1":
                print("\n=> Nova Pessoa Física")
                status, titulo, mensagem = novo_cliente(clientes)
                exibir_informacao(titulo, mensagem)
                input("\nPressione Enter para voltar ao menu principal.")
            case "2":
                print("\n=> Nova Conta")
                status, titulo, mensagem = nova_conta(agencia, contas, clientes)
                exibir_informacao(titulo, mensagem)
                input("\nPressione Enter para voltar ao menu principal.")
            case "3":
                print("\n=> Listar Clientes")
                listar_clientes(clientes)
                input("\nPressione Enter para voltar ao menu principal.")
            case "4":
                print("\n=> Listar Contas")
                listar_todas_contas(contas)
                input("\nPressione Enter para voltar ao menu principal.")
            case "5":
                print("\n=> Depositar")
                status, titulo, mensagem = depositar(contas, clientes)
                exibir_informacao(titulo, mensagem)
                input("\nPressione Enter para voltar ao menu principal.")
            case "6":
                print("\n=> Sacar")
                status, titulo, mensagem = sacar(contas, clientes)
                exibir_informacao(titulo, mensagem)
                input("\nPressione Enter para voltar ao menu principal.")
            case "7":
                print("\n=> Extrato")
                extrato(contas, clientes)
                input("\nPressione Enter para voltar ao menu principal.")
            case "8":
                print("\nℹ Encerrando aplicação...")
                sair = True
            case _:
                print("❌ Opção inválida!")
                input("\nPressione Enter para voltar ao menu principal.")

if __name__ == "__main__":
    main()

import textwrap

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        return transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def __str__(self):
        return textwrap.dedent(f"""
            Nome:                {self.nome}
            Data de Nascimento:  {self.data_nascimento}
            CPF:                 {self.cpf}
            Endereço:            {self.endereco}
            Lista de Contas:     {self.listar_contas_cliente()}
        """)


    def listar_contas_cliente(self):
        texto = ""
        for conta in self.contas:
            texto += f"\n                    Agência: {conta.agencia} | Conta: {conta.numero}"
        return texto if texto else "Nenhuma conta associada."


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

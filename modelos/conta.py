from modelos.historico import Historico
import textwrap

class Conta:
    def __init__(self, numero, agencia, cliente):
        self._saldo = 0.00
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def __str__(self):
        return textwrap.dedent(f"""
            Agência:            {self.agencia}
            Conta:              {self.numero}
            Tipo:               {self._tipo}
            Cliente:            {self.cliente.nome}
            CPF do Cliente:     {self.cliente.cpf}
        """)

    def sacar(self, valor):
        if valor > self.saldo:
            return (False, "❌ FALHA NA OPERAÇÃO", f"Você não possui saldo suficiente.\nSeu saldo é {self.saldo:.2f}")

        elif valor > 0:
            self._saldo -= valor
            return (True, "✅ SUCESSO", f"Saque realizado com sucesso!\nSeu saldo é {self.saldo:.2f}")

        else:
            return (False, "❌ FALHA NA OPERAÇÃO", "O valor informado é inválido.")

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return (True, "✅ SUCESSO", f"Depósito realizado com sucesso! \nSeu novo saldo é {self.saldo:.2f}")
        else:
            return (False, "❌ FALHA NA OPERAÇÃO", "O valor informado para depósito é inválido.")


class ContaCorrente(Conta):
    def __init__(self, numero, agencia, cliente, limite=1000.00, limite_saques=3):
        super().__init__(numero, agencia, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        self._tipo = "Conta Corrente"

    def sacar(self, valor):
        if (valor > self.limite):
            return (False, "❌ FALHA NA OPERAÇÃO", f"Você excedeu o limite para saque. \nO seu limite de valor por saque é de {self.limite:.2f}.")
        else:
            quantidade_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == "Saque"])
            if quantidade_saques >= self.limite_saques:
                return (False, "❌ FALHA NA OPERAÇÃO", f"Você excedeu o limite de saques da sua conta. \nLimite de saques: {self.limite_saques} saque(s)")
            return super().sacar(valor)

from abc import ABC, abstractmethod

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        status_transacao, titulo, mensagem = conta.depositar(self.valor)

        if status_transacao:
            conta.historico.adicionar_transacao(self)

        return status_transacao, titulo, mensagem

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        status_transacao, titulo, mensagem = conta.sacar(self.valor)

        if status_transacao:
            conta.historico.adicionar_transacao(self)

        return status_transacao, titulo, mensagem

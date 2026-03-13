from datetime import datetime

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def __str__(self):
        if not self._transacoes:
            return "Não há transações realizadas."
        
        relatorio = ""
        for transacao in self._transacoes:
            relatorio += f"{transacao['tipo']}: {transacao['valor']:.2f} - {transacao['data']}\n"
        return relatorio

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            }
        )

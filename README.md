# 🏦 Sistema Bancário em POO com Python

Projeto desenvolvido como parte do **Desafio "Modelando o Sistema Bancário em POO com Python"** da [Digital Innovation One (DIO)](https://www.dio.me/).

O objetivo é aplicar conceitos de **Programação Orientada a Objetos** na construção de um sistema bancário via terminal, utilizando herança, polimorfismo, encapsulamento e classes abstratas.

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.12+**
- Biblioteca padrão: `abc`, `datetime`, `textwrap`, `random`

---

## 📁 Estrutura do Projeto

```
desafio_conta_bancaria/
├── main.py                  # Interface CLI e ponto de entrada
└── modelos/                 # Pacote com as classes de domínio
    ├── __init__.py
    ├── cliente.py            # Classes Cliente e PessoaFisica
    ├── conta.py              # Classes Conta e ContaCorrente
    ├── historico.py          # Classe Historico
    └── transacao.py          # Classes abstratas Transacao, Deposito e Saque
```

---

## 🚀 Funcionalidades

| Opção | Funcionalidade | Descrição |
|:---:|---|---|
| 1 | **Nova Pessoa Física** | Cadastra um novo cliente informando nome, CPF, data de nascimento e endereço. |
| 2 | **Nova Conta** | Cria uma conta corrente vinculada a um cliente existente (por CPF). |
| 3 | **Listar Clientes** | Exibe todos os clientes cadastrados e suas respectivas contas. |
| 4 | **Listar Contas** | Exibe todas as contas correntes do sistema. |
| 5 | **Depositar** | Realiza um depósito em uma conta do cliente selecionado. |
| 6 | **Sacar** | Realiza um saque respeitando o limite por operação (R$ 1.000,00) e o limite de 3 saques diários. |
| 7 | **Extrato** | Exibe o histórico de transações e o saldo atual de uma conta. |
| 8 | **Sair** | Encerra a aplicação. |

---

## 🧱 Conceitos de POO Aplicados

- **Herança**: `PessoaFisica` herda de `Cliente`; `ContaCorrente` herda de `Conta`.
- **Polimorfismo**: `Deposito` e `Saque` implementam o método abstrato `registrar` da classe `Transacao`.
- **Encapsulamento**: Atributos protegidos com `_` e acesso controlado via `@property`.
- **Classes Abstratas**: `Transacao` utiliza `ABC` e `@abstractmethod` para definir a interface.

---

## ▶️ Como Executar

### Pré-requisitos

- [Python 3.12](https://www.python.org/downloads/) ou superior instalado.

### Passo a passo

1. Clone o repositório:
```bash
git clone https://github.com/lucastnsoares/desafio_conta_bancaria.git
```

2. Acesse a pasta do projeto:
```bash
cd desafio_conta_bancaria
```

3. Execute a aplicação:
```bash
python3 main.py
```

4. Navegue pelo menu digitando o número da opção desejada e pressionando **Enter**.


---
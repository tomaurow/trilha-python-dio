import datetime

class Banco:
    def __init__(self):
        self.saldo = 0
        self.movimentacoes = []
        self.saques_dia = 0
        self.limite_saques = 3
        self.limite_valor_saque = 500

    def saque(self, valor):
        if self.saques_dia >= self.limite_saques:
            print("Limite de saques diários atingido.")
            return

        if valor > self.limite_valor_saque:
            print(f"Não é possível sacar mais que R$ {self.limite_valor_saque} por saque.")
            return

        if valor > self.saldo:
            print("Você não tem saldo insuficiente para saque.")
            return

        self.saldo -= valor
        self.saques_dia += 1
        data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.movimentacoes.append(f"Saque de R$ {valor:.2f} em {data}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {self.saldo:.2f}")

    def deposito(self, valor):
        if valor <= 0:
            print("Valor de depósito inválido. Não são permitidos valores negativos ou zero.")
            return

        self.saldo += valor
        data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.movimentacoes.append(f"Depósito de R$ {valor:.2f} em {data}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {self.saldo:.2f}")

    def extrato(self):
        if not self.movimentacoes:
            print("Nenhuma movimentação realizada.")
        else:
            print("Extrato de movimentações:")
            for movimentacao in self.movimentacoes:
                print(movimentacao)
        print(f"Saldo atual: R$ {self.saldo:.2f}")

    def reset_saques_diarios(self):
        self.saques_dia = 0

def menu():
    banco = Banco()

    while True:
        print("\nMenu Banco:")
        print("1. Saque")
        print("2. Depósito")
        print("3. Extrato")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor do saque: "))
            banco.saque(valor)

        elif opcao == '2':
            valor = float(input("Digite o valor do depósito: "))
            banco.deposito(valor)

        elif opcao == '3':
            banco.extrato()

        elif opcao == '4':
            print("Obrigado por usar nosso caixa eletrônico! Sistema finalizado com segurança.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
#TODO Caixa Eletrônico (ATM) Avançado Desenvolva um simulador de caixa eletrônico.
#  O programa deve exibir um menu contínuo com as opções: 1 - Depositar, 2 - Sacar, 3 - Consultar Saldo, 4 - Sair.
#  O saldo inicial é zero. Crie uma função para lidar com o saque, que receba o saldo atual e o valor desejado. 
# A função deve verificar se há saldo suficiente. Se não houver, deve exibir uma mensagem de erro. Desafio extra no saque: Se o saque for aprovado, o programa deve utilizar uma lógica de repetição e decisões (ou restos de divisão) para calcular e exibir a quantidade de notas de R 50, 𝑅20 e R$ 10 necessárias para entregar o valor, priorizando sempre as notas maiores. 
# (Considere que o caixa só aceita saques múltiplos de 10). 


def realizar_saque(saldo, valor):
    if valor <= 0:
        print("Valor de saque inválido!")
        return saldo

    if valor % 10 != 0:
        print("O saque deve ser múltiplo de R$ 10.")
        return saldo

    if valor > saldo:
        print("Erro: saldo insuficiente!")
        return saldo

    saldo -= valor
    restante = valor

    notas50 = restante // 50
    restante %= 50

    notas20 = restante // 20
    restante %= 20

    notas10 = restante // 10
    restante %= 10

    print("Saque realizado com sucesso!")
    print("Notas entregues:")

    if notas50 > 0:
        print(f"Notas de R$ 50: {notas50}")
    if notas20 > 0:
        print(f"Notas de R$ 20: {notas20}")
    if notas10 > 0:
        print(f"Notas de R$ 10: {notas10}")

    return saldo


saldo = 0.0

while True:
    print("\n===== CAIXA ELETRÔNICO =====")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Consultar Saldo")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            print("Depósito realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    elif opcao == "2":
        valor = int(input("Digite o valor do saque: R$ "))
        saldo = realizar_saque(saldo, valor)

    elif opcao == "3":
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "4":
        print("Obrigado por utilizar o caixa eletrônico!")
        break

    else:
        print("Opção inválida! Escolha de 1 a 4.")


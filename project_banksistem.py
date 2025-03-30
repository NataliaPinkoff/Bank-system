def exibir_menu():
    print("\n=== Sistema Bancário ===")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato")
    print("0 - Sair")

def deposito(saldo, extrato, valor):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("O valor do depósito deve ser positivo.")
    return saldo, extrato

def saque(saldo, extrato, valor, saques_diarios):
    LIMITE_SAQUES = 3
    LIMITE_VALOR = 500

    if saques_diarios >= LIMITE_SAQUES:
        print("Limite diário de saques atingido.")
    elif valor > LIMITE_VALOR:
        print("O valor do saque excede o limite de R$ 500.")
    elif valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
    elif valor <= 0:
        print("O valor do saque deve ser positivo.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        saques_diarios += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato, saques_diarios

def exibir_extrato(extrato, saldo):
    print("\n=== Extrato ===")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for operacao in extrato:
            print(operacao)
        print(f"\nSaldo atual: R$ {saldo:.2f}")

def main():
    saldo = 0.0
    extrato = []
    saques_diarios = 0

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: R$ "))
            saldo, extrato = deposito(saldo, extrato, valor)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: R$ "))
            saldo, extrato, saques_diarios = saque(saldo, extrato, valor, saques_diarios)

        elif opcao == "3":
            exibir_extrato(extrato, saldo)

        elif opcao == "0":
            print("Obrigado por utilizar o sistema bancário.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

from datetime import datetime

def exibir_menu():
    print("\n=== Sistema Bancário ===")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato")
    print("0 - Sair")

def registrar_transacao(extrato, tipo, valor):
    agora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    extrato.append(f"{agora} - {tipo}: R$ {valor:.2f}")
    return extrato

def deposito(saldo, extrato, valor, transacoes_diarias, LIMITE_TRANSACOES):
    if transacoes_diarias >= LIMITE_TRANSACOES:
        print("⚠️ Limite diário de transações atingido. Tente novamente amanhã.")
    elif valor > 0:
        saldo += valor
        extrato = registrar_transacao(extrato, "Depósito", valor)
        transacoes_diarias += 1
        print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("❌ O valor do depósito deve ser positivo.")
    return saldo, extrato, transacoes_diarias

def saque(saldo, extrato, valor, saques_diarios, transacoes_diarias, LIMITE_TRANSACOES):
    LIMITE_SAQUES = 3
    LIMITE_VALOR = 500

    if transacoes_diarias >= LIMITE_TRANSACOES:
        print("⚠️ Limite diário de transações atingido. Tente novamente amanhã.")
    elif saques_diarios >= LIMITE_SAQUES:
        print("⚠️ Limite diário de saques atingido.")
    elif valor > LIMITE_VALOR:
        print("⚠️ O valor do saque excede o limite de R$ 500.")
    elif valor > saldo:
        print("⚠️ Saldo insuficiente para realizar o saque.")
    elif valor <= 0:
        print("❌ O valor do saque deve ser positivo.")
    else:
        saldo -= valor
        extrato = registrar_transacao(extrato, "Saque", valor)
        saques_diarios += 1
        transacoes_diarias += 1
        print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato, saques_diarios, transacoes_diarias

def exibir_extrato(extrato, saldo):
    print("\n📄 === Extrato ===")
    if not extrato:
        print("Nenhuma movimentação registrada.")
    else:
        for operacao in extrato:
            print(operacao)
        print(f"\n💰 Saldo atual: R$ {saldo:.2f}")

def main():
    saldo = 0.0
    extrato = []
    saques_diarios = 0
    transacoes_diarias = 0
    LIMITE_TRANSACOES = 10

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: R$ "))
            saldo, extrato, transacoes_diarias = deposito(saldo, extrato, valor, transacoes_diarias, LIMITE_TRANSACOES)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: R$ "))
            saldo, extrato, saques_diarios, transacoes_diarias = saque(saldo, extrato, valor, saques_diarios, transacoes_diarias, LIMITE_TRANSACOES)

        elif opcao == "3":
            exibir_extrato(extrato, saldo)

        elif opcao == "0":
            print("👋 Obrigado por utilizar o sistema bancário.")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

from datetime import datetime

usuarios = []
contas = []

def exibir_menu():
    print("\n=== Sistema Bancário ===")
    print("1 - Novo Usuário")
    print("2 - Nova Conta")
    print("3 - Listar Contas")
    print("4 - Acessar Conta")
    print("0 - Sair")

def menu_conta():
    print("\n=== Menu da Conta ===")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato")
    print("0 - Voltar")

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

def criar_usuario():
    cpf = input("Informe o CPF (apenas números): ")
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
    if usuario:
        print("⚠️ Já existe um usuário com esse CPF.")
        return
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Endereço (logradouro, nº - bairro - cidade/estado): ")
    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    print("✅ Usuário criado com sucesso!")

def criar_conta():
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
    if not usuario:
        print("❌ Usuário não encontrado. Cadastre o usuário primeiro.")
        return
    numero_conta = len(contas) + 1
    conta = {
        "agencia": "0001",
        "numero": numero_conta,
        "usuario": usuario,
        "saldo": 0.0,
        "extrato": [],
        "saques_diarios": 0,
        "transacoes_diarias": 0
    }
    contas.append(conta)
    print(f"✅ Conta criada com sucesso! Agência: 0001 | Número da conta: {numero_conta}")

def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
    for conta in contas:
        print(f"\nAgência: {conta['agencia']}\nConta: {conta['numero']}\nTitular: {conta['usuario']['nome']}")

def acessar_conta():
    numero = int(input("Digite o número da conta: "))
    conta = next((c for c in contas if c["numero"] == numero), None)
    if not conta:
        print("❌ Conta não encontrada.")
        return

    while True:
        menu_conta()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: R$ "))
            conta["saldo"], conta["extrato"], conta["transacoes_diarias"] = deposito(
                conta["saldo"], conta["extrato"], valor, conta["transacoes_diarias"], 10)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: R$ "))
            conta["saldo"], conta["extrato"], conta["saques_diarios"], conta["transacoes_diarias"] = saque(
                conta["saldo"], conta["extrato"], valor, conta["saques_diarios"], conta["transacoes_diarias"], 10)

        elif opcao == "3":
            exibir_extrato(conta["extrato"], conta["saldo"])

        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida.")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_usuario()
        elif opcao == "2":
            criar_conta()
        elif opcao == "3":
            listar_contas()
        elif opcao == "4":
            acessar_conta()
        elif opcao == "0":
            print("👋 Obrigado por utilizar o sistema bancário.")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

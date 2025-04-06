from datetime import datetime

# Global lists to store users and accounts
users = []
accounts = []

def display_main_menu():
    print("\n=== Banking System ===")
    print("1 - New User")
    print("2 - New Account")
    print("3 - List Accounts")
    print("4 - Access Account")
    print("0 - Exit")

def account_menu():
    print("\n=== Account Menu ===")
    print("1 - Deposit")
    print("2 - Withdraw")
    print("3 - Statement")
    print("0 - Back")

def record_transaction(statement, type_, amount):
    now = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    statement.append(f"{now} - {type_}: $ {amount:.2f}")
    return statement

def deposit(balance, statement, amount, daily_transactions, TRANSACTION_LIMIT):
    if daily_transactions >= TRANSACTION_LIMIT:
        print("⚠️ Daily transaction limit reached.")
    elif amount > 0:
        balance += amount
        statement = record_transaction(statement, "Deposit", amount)
        daily_transactions += 1
        print(f"✅ Successfully deposited $ {amount:.2f}")
    else:
        print("❌ Deposit amount must be positive.")
    return balance, statement, daily_transactions

def withdraw(balance, statement, amount, daily_withdrawals, daily_transactions, TRANSACTION_LIMIT):
    WITHDRAWAL_LIMIT = 3
    AMOUNT_LIMIT = 500

    if daily_transactions >= TRANSACTION_LIMIT:
        print("⚠️ Daily transaction limit reached.")
    elif daily_withdrawals >= WITHDRAWAL_LIMIT:
        print("⚠️ Daily withdrawal limit reached.")
    elif amount > AMOUNT_LIMIT:
        print("⚠️ Withdrawal amount exceeds $500 limit.")
    elif amount > balance:
        print("⚠️ Insufficient balance.")
    elif amount <= 0:
        print("❌ Withdrawal amount must be positive.")
    else:
        balance -= amount
        statement = record_transaction(statement, "Withdrawal", amount)
        daily_withdrawals += 1
        daily_transactions += 1
        print(f"✅ Successfully withdrew $ {amount:.2f}")
    return balance, statement, daily_withdrawals, daily_transactions

def show_statement(statement, balance):
    print("\n📄 === Statement ===")
    if not statement:
        print("No transactions recorded.")
    else:
        for entry in statement:
            print(entry)
        print(f"\n💰 Current balance: $ {balance:.2f}")

def create_user():
    cpf = input("Enter CPF (numbers only): ")
    user = next((u for u in users if u["cpf"] == cpf), None)
    if user:
        print("⚠️ A user with this CPF already exists.")
        return

    name = input("Full name: ")
    birth_date = input("Birth date (dd/mm/yyyy): ")
    address = input("Address (street, number - district - city/state): ")

    users.append({
        "name": name,
        "cpf": cpf,
        "birth_date": birth_date,
        "address": address
    })
    print("✅ User created successfully!")

def create_account():
    cpf = input("Enter user's CPF: ")
    user = next((u for u in users if u["cpf"] == cpf), None)
    if not user:
        print("❌ User not found.")
        return

    account_number = len(accounts) + 1
    account = {
        "agency": "0001",
        "number": account_number,
        "user": user,
        "balance": 0.0,
        "statement": [],
        "daily_withdrawals": 0,
        "daily_transactions": 0
    }
    accounts.append(account)
    print(f"✅ Account created successfully! Agency: 0001 | Account: {account_number}")

def list_accounts():
    if not accounts:
        print("No accounts registered.")
    for account in accounts:
        print(f"\nAgency: {account['agency']}\nAccount: {account['number']}\nHolder: {account['user']['name']}")

def access_account():
    number = int(input("Enter account number: "))
    account = next((a for a in accounts if a["number"] == number), None)
    if not account:
        print("❌ Account not found.")
        return

    while True:
        account_menu()
        option = input("Choose an option: ")

        if option == "1":
            amount = float(input("Deposit amount: $ "))
            account["balance"], account["statement"], account["daily_transactions"] = deposit(
                account["balance"], account["statement"], amount, account["daily_transactions"], 10)

        elif option == "2":
            amount = float(input("Withdrawal amount: $ "))
            account["balance"], account["statement"], account["daily_withdrawals"], account["daily_transactions"] = withdraw(
                account["balance"], account["statement"], amount, account["daily_withdrawals"], account["daily_transactions"], 10)

        elif option == "3":
            show_statement(account["statement"], account["balance"])

        elif option == "0":
            break
        else:
            print("❌ Invalid option.")

def main():
    while True:
        display_main_menu()
        option = input("Choose an option: ")

        if option == "1":
            create_user()
        elif option == "2":
            create_account()
        elif option == "3":
            list_accounts()
        elif option == "4":
            access_account()
        elif option == "0":
            print("👋 Thank you for using our banking system.")
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()

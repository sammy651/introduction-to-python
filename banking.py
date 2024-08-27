accounts = []

class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Ksh {amount} into {self.name}'s account")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew Ksh {amount} from {self.name}'s account")

    def check_balance(self):
        print(f"{self.name}'s account balance: Ksh {self.balance}")

def create_account():
    name = input("Enter account name: ")
    initial_balance = float(input("Enter initial balance (or 0 for new account): "))
    account = Account(name, initial_balance)
    accounts.append(account)
    print(f"Created {account.name}'s account with initial balance Ksh {account.balance}")

def manage_account(account):
    while True:
        print(f"\nManaging {account.name}'s account. Balance: Ksh {account.balance}")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter choice (1-4): ")
        
        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            break
        else:
            print("Invalid choice, try again")

def main():
    while True:
        print("\nWelcome to the Banking App!")
        print("1. Create Account")
        print("2. Manage Existing Account")
        print("3. Exit")
        
        choice = input("Enter choice (1-3): ")
        
        if choice == "1":
            create_account()
        elif choice == "2":
            if not accounts:
                print("No accounts exist. Create an account first.")
            else:
                print("Select an account:")
                for i, account in enumerate(accounts):
                    print(f"{i+1}. {account.name}" )
                index = int(input("Enter account number: ")) - 1
                if index < 0 or index >= len(accounts):
                    print("Invalid account number")
                else:
                    manage_account(accounts[index])
        elif choice == "3":
            break
        else:
            print("Invalid choice, try again")

if __name__ == "__main__":
    main()
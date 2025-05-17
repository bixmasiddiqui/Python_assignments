import random

class ATM():
    def __init__(self, name, account_number, balance=0, pin="0000"):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.pin = pin

    def verify_pin(self):
        attempts = 3
        while attempts > 0:
            entered_pin = input("Enter your 4-digit PIN: ")
            if entered_pin == self.pin:
                print("PIN verified successfully!\n")
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN. Attempts remaining: {attempts}")
        print("Too many incorrect attempts. Exiting for security reasons.")
        return False

    def account_detail(self):
        print("\n=== ACCOUNT DETAIL ===")
        print(f"Account Holder: {self.name.upper()}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Balance: Nu. {self.balance}\n")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Nu. {amount} deposited successfully.")
        print(f"Current Balance: Nu. {self.balance}\n")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance!")
            print(f"Your balance is Nu. {self.balance} only\n")
        else:
            self.balance -= amount
            print(f"Nu. {amount} withdrawal successful!")
            print(f"Remaining Balance: Nu. {self.balance}\n")

    def check_balance(self):
        print(f"Your current balance is: Nu. {self.balance}\n")

    def transaction(self):
        if not self.verify_pin():
            return
        while True:
            print("===== ATM MENU =====")
            print("1. Account Details")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Exit")

            choice = input("Choose an option (1-5): ")

            if choice == '1':
                self.account_detail()
            elif choice == '2':
                amount = float(input("Enter amount to deposit: "))
                self.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter amount to withdraw: "))
                self.withdraw(amount)
            elif choice == '4':
                self.check_balance()
            elif choice == '5':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    print("=== Welcome to ATM Setup ===")
    name = input("Enter your name: ")
    pin = input("Set a 4-digit PIN for your account: ")

    while len(pin) != 4 or not pin.isdigit():
        print("Invalid PIN. It must be 4 digits.")
        pin = input("Set a 4-digit PIN for your account: ")

    account_number = str(random.randint(10000000, 99999999))
    atm_user = ATM(name, account_number, balance=0, pin=pin)

    print(f"\nAccount created successfully! Your account number is: {account_number}\n")
    atm_user.transaction()



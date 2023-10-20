import time

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

def check_sufficient_balance(func):
    def wrapper(self, amount):
        if amount > self.balance:
            print("Invalid amount: Insufficient balance.")
        else:
            func(self, amount)
    return wrapper

class BankAccount:
    def __init__(self, initial_balance = 0):
        self.account_number = account_number
        self.balance = initial_balance
        self.transaction_history = []
        
    @measure_execution_time
    def deposit(self, amount):
        self.balance = self.balance + amount
        self._add_transaction("Deposit", amount)
    
    @measure_execution_time
    @check_sufficient_balance
    def withdraw(self, amount):
            self.balance = self.balance - amount
            self._add_transaction("Withdrawal", amount)
    
    def get_balance(self):
        return self.balance 
    
    def closure(self, amount):
            self.balance== 0
            "account is closed"
            
    def get_transaction_history(self):
        return self.transaction_history
    
    def generate_statement(self):
        print("\n--- Account Statement ---")
        for transaction in self.transaction_history:
            print(f"{transaction['type']} - Amount: {transaction['amount']}, Timestamp: {transaction['timestamp']}")
        print(f"Current Balance: {self.balance}")
        print()
        
    def _add_transaction(self, transaction_type, amount):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        transaction = {'type': transaction_type, 'amount': amount, 'timestamp': timestamp}
        self.transaction_history.append(transaction)
        
    def generate_summary(self):
        print("\n--- Account Summary ---")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.balance}")
        print(f"Number of Transactions: {len(self.transaction_history)}")
    
    def is_account_closed(self):
        return self.balance == 0 and not self.transaction_history
    
    def close_account(self):
        self.balance = 0
        self.transaction_history.clear()
        print("\n"+"-"*55,"\n")
        print("Account closed successfully.")
        print("\n"+"-"*55,"\n")
    
class Menu:
    first = True
    def __init__(self):
        self.options = []
    
    def add_option(self, option):
        self.options.append(option)
        
    def get_input(self):
        done = False

        while not done:
            for i in range(len(self.options)):
                print("%d %s" % (i+1, self.options[i]))
            try:
                user_choice = int(input("Enter your option: "))
                if (user_choice >= 1 and user_choice <= len(self.options)):
                    done = True
                    return user_choice      
                else:
                    print(f'\nInvalid option: You entered {user_choice} while the options ranges from 1 to 9')
                    print("Please enter a number corresponding to desierd function\n")
            except ValueError:
                print("\nInavlid option: The option must be a number")
                print("Please enter a number corresponding to desierd function\n")

main_menu = Menu()


main_menu.add_option("Create new account")
main_menu.add_option("Deposit money into the account")
main_menu.add_option("Withdraw money from the account")
main_menu.add_option("Check the current balance of the account")
main_menu.add_option("Transactions history")
main_menu.add_option("Account statement")
main_menu.add_option("Account summary")
main_menu.add_option("Check if account is active or closed")
main_menu.add_option("Close the account")
main_menu.add_option("Exit program")

while True:
    choice = main_menu.get_input()
    try:       
        
        if choice == 1:
            account_number = input("Enter account number: ")
            my_account = BankAccount(account_number)
            amount = input("Enter an initial amount to open the new account: ")
            while not (amount.replace(".","")).isdigit():
                print("Please enter a valid amount.")
                amount = input("Enter an initial amount to open the new account: ")
            
            amount = float(amount)
                
            my_account = BankAccount(amount)
        
        elif choice == 2:
            amount = float(input("\nEnter an amount to deposit into your account: "))
            while amount <= 0:
                print("\nInvalid amount: The deposit amount must be a number greater then 0")
                amount = float(input("\nEnter an amount to deposit into your account: "))
            my_account.deposit(amount)
        
        elif choice == 3:
            amount = float(input("\nEnter an amount to withdraw from your account: "))
            while amount <= 0:
                print("\nInvalid amount: The withdraw amount must be a number greater then 0")
                amount = float(input("\nEnter an amount to withdraw from your account: "))
            my_account.withdraw(amount)
            
        
        elif choice == 4:
            print("\n"+"-"*55+"\n")
            print("You current balance = ", my_account.get_balance())
            print("\n"+"-"*55,"\n")
        
        elif choice == 5:
            transactions = my_account.get_transaction_history()
            print("\n"+"-"*55+"\n")
            print("--- Transaction History ---")
            for transaction in transactions:
                print(f"{transaction['type']} - Amount: {transaction['amount']}, Timestamp: {transaction['timestamp']}")
            print("\n"+"-"*55,"\n")

        elif choice == 6:
            my_account.generate_statement()
            
        elif choice == 7:
            my_account.generate_summary()
        
        elif choice == 8:
            if my_account.is_account_closed():
                print("\n"+"-"*55+"\n")
                print("Account is closed.")
                print("\n"+"-"*55,"\n")
            else:
                print("\n"+"-"*55+"\n")
                print("Account is still open.")
                print("\n"+"-"*55,"\n")

        elif choice == 9:
            my_account.close_account()
        
        else:
            print("\n"+"-"*55+"\n")
            print("\nThank you for choosing our bank.")
            print("Bye")
            print("\n"+"-"*55,"\n")
            break
    except NameError:
        print("\n"+"-"*55+"\n")
        print("Inavlid option: A account must be created first")
        print("\n"+"-"*55,"\n")
    except ValueError:
        print("\n"+"-"*55+"\n")
        print("Invalid value: The value must be a number")
        print("\n"+"-"*55,"\n")

class BankAccount:
    def __init__(self, initial_balance = 0):
        self.balance = initial_balance
        self.account_number = 0

    def set_account_number(self):
        self.account_number =+ 1111

    def get_account_number(self):
        return self.account_number
        
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def withdraw(self, amount):
            self.balance = self.balance - amount
    
    def get_balance(self):
        return self.balance 
    
    def closure(self):
            self.balance = 0
            print("account is closed")
class Menu:
    first = True
    def __init__(self):
        self.options = []
    
    def add_option(self, option):
        self.options.append(option)
        
    def get_input(self):
        done = False
        if self.first:
            while not done:
                for i in range(len(self.options)):
                    print("%d %s" % (i+1, self.options[i]))
                user_choice = int(input("Enter your option: "))
                if (user_choice >= 1 and user_choice <= len(self.options)):
                    done = True
                else:
                    print("Invalid option.")
                    print("** Enter a valid option **")
                if user_choice == 1:
                    self.first = False
                
        else:
            while not done:
                print("\n")
                for i in range(1, len(self.options)):
                    print("%d %s" % (i+1, self.options[i]))
                user_choice = int(input("Enter your option: "))
                if (user_choice >= 2 and user_choice <= len(self.options)):
                    done = True
                else:
                    print("Invalid option.")
                    print("** Enter a valid option **")
                    
        return user_choice
    
    def reset(self):
        self.first = True

main_menu = Menu()

main_menu.add_option("Open a new account")
main_menu.add_option("Deposit money into the account")
main_menu.add_option("Withdraw money from the account")
main_menu.add_option("Check the current balance of the account")
main_menu.add_option("Keep track of all the transactions made on the account")
main_menu.add_option("Retrieve the transaction history for an account")
main_menu.add_option("Generate and print an account statement")
main_menu.add_option("Generate and print an account summary")
main_menu.add_option("Close the account")
main_menu.add_option("Account status active or closed\n")

while True:
    choice = main_menu.get_input()
    try:
        if choice == 1:
            amount = input("Enter an initial amount to open the new account: ")
            while not (amount.replace(".","")).isdigit():
                print("Please enter a valid amount.")
                amount = input("Enter an initial amount to open the new account: ")
            
            amount = float(amount)
            my_account = BankAccount(amount)
            my_account.set_account_number()
            
        
        elif choice == 2:
            amount = float(input("Enter an amount to deposit into your account: "))
            my_account.deposit(amount)
        
        elif choice == 3:
            amount = float(input("Enter an amount to withdraw from your account: "))
            my_account.withdraw(amount)
        
        elif choice == 4:
            print("You current balance = $", my_account.get_balance())

        elif choice == 8:
            print(f"Your account number is: {my_account.get_account_number()}")
            
        elif choice == 9:
            my_account.closure()
            main_menu.reset()
            # this choice isn't working properly yet
            print("choice 9 isn't working properly yet")
        
        else:
            print("Thank you for choosing our bank.")
            print("Bye")
            break
    
    except NameError:
        print("You need to create an account first.")
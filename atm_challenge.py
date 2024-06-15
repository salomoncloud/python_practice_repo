# creating an atm 

def atm_booth():
    #Step 1 is getting user information
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    dob = input("Enter your date of birth (DD/MM/YYYY): ")

    balance = 0  #balance at start

    #ATM operation
    while True:
        print(f"Welcome {first_name}, what would you like to do today?")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Take out the card")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == '1':
            #Deposit option
            try:
                deposit_amount = float(input("How much money would you like to deposit? "))
                if deposit_amount > 0:
                    balance += deposit_amount
                    print(f"Successfully deposited ${deposit_amount}. Your new balance is ${balance:.2f}.")
                else:
                    print("Please enter a positive amount.")
            except ValueError:
                print("Please enter a valid amount.")
        
        elif choice == '2':
            #Withdrawal
            try:
                withdraw_amount = float(input("How much money would you like to withdraw? "))
                if withdraw_amount > balance:
                    print("Insufficient funds. You cannot withdraw more than your current balance.")
                elif withdraw_amount > 500:
                    print("Withdrawal limit exceeded. You cannot withdraw more than $500 at a time.")
                elif withdraw_amount > 0:
                    balance -= withdraw_amount
                    print(f"Successfully withdrew ${withdraw_amount}. Your new balance is ${balance:.2f}.")
                else:
                    print("Please enter a positive amount.")
            except ValueError:
                print("Please enter a valid amount.")
        
        elif choice == '3':
            #Removal of card
            print(f"Thank you so much, have a wonderful day {first_name}.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")
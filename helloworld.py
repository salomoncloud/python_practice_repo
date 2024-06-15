print("Hello World")

def greet(name):
    return f"hello, {name}!"

print(greet("folks"))

def how_much_money_do_i_have(money):
    return f"I've got {money} dollars!"

print (how_much_money_do_i_have(1553672))

def name_and_amount(name, amount):
    return f"{name} is {amount} times richer than us!"

print(name_and_amount("Jeff Bezos", 14489271073))


def calculate_sum(numbers):
    return sum(numbers)
input_numbers = input("Enter numbers separated by spaces: ")

numbers_list = list(map(int, input_numbers.split()))
total_sum = calculate_sum(numbers_list)
print("The sum of the numbers is:", total_sum)

def subtract_numbers(num1, num2):
    return num1 - num2

input1 = input("Enter your first number: ")
input2 = input("Enter a second number: ")

number1 = int(input1)
number2 = int(input2)

result = subtract_numbers(number1, number2)

print("The result of the subtraction is:", result)

def multiply_numbers(num1, num2):
    return num1 * num2

input1 = input("starting with: ")
input2 = input("and than: ")

number1 = int(input1)
number2 = int(input2)

result = multiply_numbers(number1, number2)

print("After multiplying we get:", result)

# literals
# can be integers like octal numbers or hexidecimal numbers, floating point numbers, stings, booleans
# operators 
# arithmetic (* or **, / or //, % modulo [remainders], +, - ) 

def fill_whitespaces_with_plus():
    user_input = input("Enter a string: ")
    result = user_input.replace(' ', '+')
    print("Modified string:", result)

def check_number_range():
    try:
        number = int(input("Enter a number: "))
        if 250 < number < 500:
            print("The number is between 250 and 500.")
        else:
            print("The number is not between 250 and 500.")
    except ValueError:
        print("Please enter a valid number.")

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

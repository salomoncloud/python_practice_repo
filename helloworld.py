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
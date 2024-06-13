# print("Hello World")
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
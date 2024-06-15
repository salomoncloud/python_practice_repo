def check_number_range():
    try:
        number = int(input("Enter a number: "))
        if 250 < number < 500:
            print("The number is between 250 and 500.")
        else:
            print("The number is not between 250 and 500.")
    except ValueError:
        print("Please enter a valid number.")
check_number_range()
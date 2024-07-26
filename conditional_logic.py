# booleans
# creating something that checks your age and license before starting a car, for example
is_old = True
is_licenced = False

if is_old and is_licenced:
    print("you are old enough to drive this car")
else:
    print('You are not eligible to drive')

# truthy values are basically values that are considered true when used in a boolean context
# falsy is the opposite
# look up python truthiness and truth table on google for example

# ternary operator
# else if shortcut for cleaner code - operation that evaluates to something based on the condition that its true or not
# condition_if_true if condition else condition_if_false
is_friend = True
can_message = "Message allowed" if is_friend else "Not allowed to message"
print(can_message)

# short circuiting
is_user = True
if is_friend and is_user:
    print("Friends")
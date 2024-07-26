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
if is_friend or is_user:
    print("Friends")

# basically our python code will look at the first condition, for ex, here because is_friend is true it wont look at user
# logical operators < > == != => =< and or not
# example of short circuiting using logical operators
print(1 < 2 > 3 < 4)

# excercise - imagine you work for ea sports and your working on a new nhl game - be a pro mode, at the nhl draft
is_Forward = False
is_top_prospect = True
is_top_scorer = True
if is_Forward and is_top_prospect:
    print("You've been selected in the first round!")
else:
    print("You will be picked later in the first round.")

draft_results = "You're going first overall!" if is_top_scorer else "You will slip to the second round"
print(draft_results)

# another example

is_criminal = False
is_innocent = True

if is_innocent and not is_criminal:
    print("You're free to go")
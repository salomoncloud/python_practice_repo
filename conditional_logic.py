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

# for loops --- run lines of code over and over and over
# ex - for (variable for each item after the in) in 'iretable':

for item in (1,2,3,4,5):
    print(item)
    print(item)
    print(item)
print(item)
     # if you were to add the print item 3 more time it would print out those set of numbers 3 more times - hence looping
# however if i add that last print the way it is- breaking that identation rule - its only going to print 5 because its only looking at its one singular set, running through that, ending at 5

# you can also nest another for loop inside of a for loop, nested loops

# iretable --- object or collection that can be iterated over- list, dictionary, tuple, set, string
# iterate --- one by one check each item in the collection
# ex

users = {
    'name': 'Borat',
    'age': 57,
    'will_get_this': True
}

for item in users.items():
    print(item)

# or we can also go straight for the values this way

for item in users.values():
    print(item)

# can do only for keys like this

for item in users.keys():
    print(item)

# we can also print seperatly the items, for example name and borat

for item in users.items():
    key, value = item
    print(key, value)
# or
for key, value in users.items():
    print(key, value)

# range() - special object that produces a sequence of int from start to stop

print(range(100)) # you will get range(0, 100) - where this can be useful is for loops

for number in range(100):
    print (number) # you will get numbers 1 to 100

# a better way is to do (0, 100) but you can also do a stepover like this (0, 100, 2) which will get to 100 by even numbers
# you can do (100, 0, -1) to descend, and can also wrap the range in a list to run these loops into organized lists
# ex
for _ in range(2):
    print(list(range(100, 0, -2)))
# escape sequences are simply adding a slash in a sentence where you would put in quotes
# example
weather = "It's \"kind of\" sunny"

print(weather)

# formatted strings
# example
name = 'salomon'
age = 26
print("hi " + name + ". Are you " + str(age) + " years old?")
# a better way to do this^ is :
name_for_example = 'fritz'
age_for_example = 27
print(f'hi {name_for_example}. You are {age_for_example} years old.') 
# that f helps us make the code cleaner

# lists - ordered sequence of objects of any type
fruits = ['apples', 
          'oranges', 
          'bananas', 
          'grapes', 
          'peaches']

veggies = ['brocoli', 
           'tomatoes', 
           'celery', 
           'salad', 
           'eggplant']

# lists are data structures - data structures are a way to organize info together
#print(fruits[2]) would print out bananas

# list slicing - similar to string slicing with the stop start and stepover
# print(fruits[0::2]) this would skip over every second one

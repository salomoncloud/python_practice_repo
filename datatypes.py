# fundamental data types - int float bool str list tuple set dict --- data types are just values, stored info that can be used
# classes - custom types of data 
# specialized data types - special modules 
# none - means nothing, zero, no value
# gonna practice math functions here
print(type(2 + 4))
print(type(2 / 4))

# math functions
print(round(3.1))
print(abs(-20))
print(abs(-1))

# operator precendence - different operators have precendents over others, like bedmas for example
print(20 - 3 * 4)
# (), than ** power of, than * and /, thans last is + - 
print((5 + 4) * 10 / 2)
# would be 45
# complex is another data type used to create a complex number from a real part and an optional imaginary part
# bin is for binary, used to store numbers in memory as binary
print(bin(14012846))
# playing with variables 
tickets = 200
ticket_buyers = tickets/2
print(ticket_buyers)
# will equal 100
seats_taken = ticket_buyers
print(seats_taken)
theatre1, theatre2, theatre3 = 11, 22, 33
print(theatre1)
print(theatre2)
print(theatre3) 

# type conversion
print(type(str(100)))
a = str(100)
b = int(a)
c = type(b)
print(c)

# string indexes, basically similar to what you learned in terraform, the first letter being index 0, second is 1, etc
# example
salomonlubin = 'this is my name'
print (salomonlubin[2])
# now when you print this it will give you 'i' because that is the 3rd letter in the string

# a python rule, when we use [], the first item between those [] is what we call the start, that means where do we want the code to look.
# but also if we do [start:stop] (adding a colon) we can tell the code where to stop
# ex
print (salomonlubin[1:8])
# should give you 'his is' because it will start at index 1 and end at 8
# next thing is stepover, this is like [start:stop:stepover] so after stopping it can step over
# ex 
random_set_of_digits = '01234567'
print (random_set_of_digits[0:8:2])
# in python, if we add a - (negative) index, it will start at the end of the string, for ex (salomonlubin[-7])

# immutability in programming means things cannot be changed
# for example, how we assigned my name as a string, after printing we will get this is my name, and we cant manipulate this or change it
# the only way is to completely re-assign the value

# built in functions and methods
# covered some earlier but here are some more
print(len('cloudcomputingishard')) # counts the length in human form
greet = 'hellohello'
print(greet[0:])
# methods have a special syntax, they start with a dot usually
quote = 'hard work pays off'
print(quote.upper())
print(quote.capitalize ())
print(quote.find ("off"))
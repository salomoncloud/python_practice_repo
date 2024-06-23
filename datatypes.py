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
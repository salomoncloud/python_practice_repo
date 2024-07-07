# tuples are like lists but immutable 
# benefits of tuple are efficient and safer code because its predictable and people wont modify it
# however tuple is less flexible
# faster than lists
# ex - uber using tuple for long/lat of location
tuple_list = [(1, 2), (3, 4), (5, 6)]

#new_tuple = tuple_list[1:3]
# will print our 3,4 and 5,6
#print(new_tuple)

x = tuple_list[0]
y = tuple_list[1]
print(x) # x will equal to 1,2
print(y) # y will equal to 3,4

#a shorter way to do this^

a,b,c, *other = (5,10,15,20,25,30)
print(a)
print(b)
print(c)
print(other)
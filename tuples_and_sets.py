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

a,b,c, *other = (5,10,15,20,20,25,30)
print(a)
print(b)
print(c)
print(other)

# tuple only has 2 methods, count and index

# count
print(other.count(20)) # will say 2 because there are 2 20's in other

# index
print(other.index(30)) # will print out 3 as this is the index of 30 in other


# sets
# unordered collections of unique objects
# ex - similar to dictionary we use {} but instead of key value its just value
my_set = {1,2,3,4,5,5}
print(my_set) # will not return duplicates, everything is unique

# to make a list into a set and remove duplicates from that list, simply do set(list) method
# could be useful when a website has email addresses that may be duplicate, you could convert that list into set to not spam email over and over

#set methods
set_of_nums = {5,10,15,20,25,30}
second_set_of_nums = {30,35,40,45,50,55}

print(set_of_nums.difference(second_set_of_nums)) # will find the differences between sets

#print(set_of_nums.discard(5))
#print(set_of_nums) these will remove 5 from the set

#print(set_of_nums.difference_update(second_set_of_nums))
#print(set_of_nums) differences are removed between the 2 sets

print(set_of_nums.intersection(second_set_of_nums)) #will print the common things between 2 sets, in this case 30 -  can also use &

print(set_of_nums.isdisjoint(second_set_of_nums)) # asks if they are overlapping, nothing in common, because of 30 it will be false

print(set_of_nums.union(second_set_of_nums)) # will join both sets and removed duplicates -  you can also use the pipe | to do this like in linux

#.issubset
#.issuperset
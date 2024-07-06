# matrix is a way to describe 2D lists - multi-dimensional lists
# ex
matrix = [
    [1,2,3],
    [2,4,6],
    [7,8,9]
]
# in this example we have the main array which is the first pair of square brackets, and than the 2nd containing the numbers
# matrix's are used for ml models and image processing, and they work with 1's and 0's
# to access things in matrix, ex:
print(matrix[0][1])

# actions that you can take on a list - methods
parking_spots = [1,2,3,4,5,2,90,3]

#adding
parking_spots.append(100)
print(parking_spots)
# this will add 100 to the list at the end

digits = [1,2,3,4,5,1]
digits.insert(4, 100)
print(digits)
# this will insert 100 at the index of 4

special_plates = [10,20,30,40,50]
special_plates.extend([1000,200,150,250])
print(special_plates)
# extends the list with whatever you added - iterates over list

#removing methods
parking_spots.pop()
print(parking_spots) # removes 100 at the end of the list, you can also specify in the () the index to be specific
# theres also remove and clear

# index
# print(digits.index(2)) will tell you what is at the index mentioned
print(digits.index(3, 0, 4)) # starting by telling your function what you need, than start section and end

# to look for something in a list
print(500 in special_plates)
#it will say false, works the same for ex: 
print("w" in "I will get hired by google one day")

#count
print(digits.count(1))

#sort
parking_spots.sort()
print(parking_spots)
# this will sort things in order, moving bigger numbers to the back end of the list for example

#sorted will do the same but less lines of code because its a function
print(sorted(parking_spots))
# sorted produces a new array, but if you print the list without sorted it will revert back to og

# reverse, does as its name implies - reversing in place
special_plates.sort()
special_plates.reverse()
print(special_plates)
# this will sort in reverse

# common list patterns
special_plates.sort()
special_plates.reverse()
print(special_plates[::-1])
# line by line, i sorted so its in order, than reversed, than reversed again but instead of being in reverse its now in order
# as a refresher, :: is slicing the list- start:stop:indexjump is the rule

# range
# generating a list quickly, ex:
# print(list(range(1,100)))
# its going to generate a full list from 1-99 in list form, and you can even just leave 100 and it will do the same

# .join
# this works on strings, ex:
sentence = ' ' # an empty space
final_sentence = sentence.join(['hey', 'python', 'is', 'fun'])
print(final_sentence)
# this will create a sentence that will have a space between each string created, joining the space with the strings
# what you could have done actually is simply this:
morning_news = ' '.join(['world', 'peace', 'is', 'here'])
print(morning_news)

# list unpacking 
#ex list:
# basket = [1,2,3] what if i want to assign a variable to each item?
# this is how
a,b,c = [1,2,3]
print(a)
print(b)
print(c)

# what if we have a longer list but only want the first 3 to have individual variables, but the rest under one variable?
e,f,g,*other = [4,5,6,7,8,9]
print(other)

# none - used to represent the absence of value, for example
weapons = None # like how in a game we start off with no weapons

# dictionary - dict - data type/data structure, looks like:

dictionary = {
'a': 1,
'b': 2
}
# curly braces are for dictionaries, and they work with key/value pairs
#to access these:
print(dictionary['b'])
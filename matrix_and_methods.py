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
special_plates.extend([150,250])
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


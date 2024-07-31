# using looping, im gonna practice here a loop over an iterable list and sum up the total of the list

waiting_list = [1,2,3,4,5,6,7,8,9,10]

counter = 0
for item in waiting_list:
    counter = counter + item

print(counter)

# loop runs code over and over after every value, so setting a counter variable outside the loop you can ensure that counter wont change after adding every piece of the list
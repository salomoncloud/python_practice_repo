# Checking prime numbers
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Test the function
num = int(input("Enter the number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

    # fibonacci calculations


# display the Fibonacci sequence up to defined term

# Prompt user to input the number of terms they want in the Fibonacci sequence
nterms = int(input("How many terms? "))

# first two terms of the Fibonacci sequence
n1, n2 = 0, 1

# counter to keep track of the number of terms generated
count = 0

# check if the number of terms is valid (must be a positive integer)
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return the first term (n1)
elif nterms == 1:
   print("Fibonacci sequence up to", nterms, ":")
   print(n1)
# generate Fibonacci sequence for n terms
else:
   print("Fibonacci sequence:")
   # loop to generate the Fibonacci sequence
   while count < nterms:
       # print the current term in the sequence
       print(n1)
       # calculate the next term in the sequence
       nth = n1 + n2
       # update the values of n1 and n2 to the next terms in the sequence
       n1 = n2
       n2 = nth
       # increment the counter by 1
       count += 1

# common elements between two lists
# both sets using intersection function
# sets
def common_member(a, b): 
	a_set = set(a)
	b_set = set(b)
	
	# check length 
	if len(a_set.intersection(b_set)) > 0:
		return(a_set.intersection(b_set)) 
	else:
		return("no common elements")
	

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_member(a, b))

a =[405, 66, 2, 1111, 5]
b =[648, 22, 38, 5]
print(common_member(a, b))


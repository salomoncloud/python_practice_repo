def factorial(n):
    # n is the parameter of the function, which will take the value for which we want to calculate the factorial
    if n == 0:
        return 1
    # stops the recursion from continuing indefinitely
    else:
        return n * factorial(n - 1)
# multiplied by the result of calling the factorial function
result = factorial(3)
# starts the recursion process to calculate the factorial
print(result)
# so a good example to think of is inception with its layers of dreams - note that down

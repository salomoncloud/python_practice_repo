def factorial(n):
    # n is the parameter of the function, which will take the value for which we want to calculate the factorial
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# calculate factorial
result = factorial(3)
print(result)

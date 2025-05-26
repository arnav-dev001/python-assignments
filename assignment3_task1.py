def factorial(n):
    n = int(n)
    if n < 2:
        return 1
    else:
        return n * (factorial(n-1))

input = input("Enter a number: ")
result = factorial(input)
print("Factorial of", input,"is:", result)

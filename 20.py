def Factorial(n):
    return 1 if n <= 1 else n*(Factorial(n-1))

sumdigits = sum(int(digit) for digit in str(Factorial(100)))
print(sumdigits)
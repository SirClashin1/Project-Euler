def Factorial(n):
    return 1 if n <= 1 else n*(Factorial(n-1))

sumdigits = 0
for digit in str(Factorial(100)):
    sumdigits += int(digit)
print(sumdigits)
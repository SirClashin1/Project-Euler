def square(a):
    return a * a
SumSquare = 0; sum = 0
for i in range(1, 101):
    SumSquare += square(i)
    sum += i
print(square(sum) - SumSquare)


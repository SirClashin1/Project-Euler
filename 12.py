def TriangleNumber(n):
    TriangleNumber = 0
    for i in range(1, n+1):
        TriangleNumber += i
    return TriangleNumber
def iNumDivisors(n):
    iNumDivisors = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            iNumDivisors += 2
    if n**0.5 == int(n**0.5):
        iNumDivisors -= 1
    return iNumDivisors
i = 1
while iNumDivisors(TriangleNumber(i)) < 500:
    i += 1
print(TriangleNumber(i))
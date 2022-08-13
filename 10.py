def SieveUpTo(a):
    IsPrime = [True for i in range(a+1)]
    ListOfPrimes = []
    n = 2
    while n*n <= a:
        if IsPrime[n]:
            for i in range(n*n, a+1, n):
                IsPrime[i] = False
        n += 1
    for j in range(2, a+1):
        if IsPrime[j]:
            ListOfPrimes.append(j)
    return sum(ListOfPrimes)
print(SieveUpTo(2000000))
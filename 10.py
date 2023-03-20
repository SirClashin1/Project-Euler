def SieveUpTo(a):
    IsPrime = [True for _ in range(a+1)]
    n = 2
    while n**2 <= a:
        if IsPrime[n]:
            for i in range(n**2, a+1, n):
                IsPrime[i] = False
        n += 1
    ListOfPrimes = [j for j in range(2, a+1) if IsPrime[j]]
    return sum(ListOfPrimes)
print(SieveUpTo(2000000))
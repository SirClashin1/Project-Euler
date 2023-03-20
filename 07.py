def isPrime(a) -> bool:
    if a in [2, 3]:
        return True
    elif a % 2 == 0 or a % 3 == 0:
        return False
    else:
        i = 5
        while i**2 <= a:
            if a % i == 0:
                return False
            i += 2
        return True

def nthPrime(n):
    if n == 2:
        return
    primes = [2]
    i = 1
    while len(primes) < n:
        i += 2
        if isPrime(i):
            primes.append(i)
    return primes[-1]
print(nthPrime(10001))
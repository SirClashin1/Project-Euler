num = 600851475143
def isPrime(n): 
    for i in range(2, int(n**0.5 + 1)):
        if n % i == 0:
            return False
    return True

for j in range(1, int(num**0.5 + 1)):
    if num%j == 0 and isPrime(j):
        print(j)

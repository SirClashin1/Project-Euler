num = 600851475143
def isPrime(n): 
    return all(n % i != 0 for i in range(2, int(n**0.5 + 1)))

for j in range(1, int(num**0.5 + 1)):
    if num%j == 0 and isPrime(j):
        print(j)

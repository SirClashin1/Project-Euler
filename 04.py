Answer = -1

def isPalindrome(n):
    return str(n)[::-1] == str(n)

for i in range(1000):
    for j in range(i):
        product = i*j
        if isPalindrome(product):
            Answer = max(Answer, product)
print(Answer)


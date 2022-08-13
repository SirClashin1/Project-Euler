Answer = -1

def isPalindrome(n):
    if str(n)[::-1] == str(n):
        return True
    return False

for i in range(0, 1000):
    for j in range(0, i):
        product = i*j
        if isPalindrome(product):
            Answer = max(Answer, product)
print(Answer)


def DivByUpTo(a):
    num = 1
    while True:
        for i in range(1, a+1):
            if num % i != 0:
                break
            if i == a:
                return num
        num += 1
print(DivByUpTo(20))
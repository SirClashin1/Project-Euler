list_amicables = []
def sumdivisors(n):
    total = 1
    for x in range(2, int(n**0.5 + 1)):
        if n % x == 0:
            total += x
            y = n // x
            if y > x:
                total += y
    return total
for i in range(1, 10001):
    for j in range(i+1, 10001):
        if sumdivisors(i) == j and sumdivisors(j) == i:
            list_amicables.append(i)
            list_amicables.append(j)
print(sum(list_amicables))
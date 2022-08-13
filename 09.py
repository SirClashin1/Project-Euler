def sq(a):
    return a*a
for c in range(1, 1001):
    for b in range(1, c):
        for a in range(1, b):
            if a + b + c == 1000:
                if sq(a) + sq(b) == sq(c):
                    print(a*b*c)
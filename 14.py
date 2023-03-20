def NumOfCollatzSteps(n):
    steps = 0
    while n > 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps
Max_Steps = -1
for i in range(1, 1000001):
    Steps = NumOfCollatzSteps(i)
    if Steps > Max_Steps:
        Max_Steps = Steps
        print(i) #Last i printed is the solution
    
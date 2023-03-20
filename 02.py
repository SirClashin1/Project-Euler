Temp, Sequence_current, Previous_num, Counter = 0, 1, 0, 0
while Sequence_current < 4000000:
    if Sequence_current%2:
        Counter += Sequence_current
    Sequence_current, Previous_num = Sequence_current + Previous_num, Sequence_current

print(Counter)
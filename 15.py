from ftplib import ftpcp
from math import factorial as ft
def BinomialCoefficient(a, b):
    return ft(a) // (ft(b) * ft(a - b))
print(BinomialCoefficient(20+20, 20))



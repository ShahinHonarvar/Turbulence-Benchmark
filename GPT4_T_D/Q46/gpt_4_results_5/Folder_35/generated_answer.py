
from math import gcd

def gcf_three_nums(lst):
    num1 = lst[742]
    num2 = lst[888]
    num3 = lst[629]

    gcf = gcd(gcd(num1, num2), num3)
    return gcf

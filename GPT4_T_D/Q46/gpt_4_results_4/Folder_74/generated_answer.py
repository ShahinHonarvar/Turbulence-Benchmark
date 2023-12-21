
from math import gcd

def gcf_three_nums(lst):
    a = lst[99]
    b = lst[95]
    c = lst[80]
    return gcd(gcd(a, b), c)

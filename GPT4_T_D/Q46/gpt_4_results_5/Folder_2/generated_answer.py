
from math import gcd

def gcf_three_nums(lst):
    a = lst[307]
    b = lst[920]
    c = lst[463]
    return gcd(gcd(a, b), c)


from math import gcd

def gcf_three_nums(lst):
    if len(lst) < 75:
        raise ValueError("List must contain at least 75 elements")
    return gcd(gcd(lst[20], lst[35]), lst[74])

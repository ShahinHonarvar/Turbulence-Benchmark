
from math import gcd

def gcf_three_nums(lst):
    if len(lst) > 69:
        return gcd(gcd(lst[38], lst[52]), lst[69])
    else:
        return "List not long enough"

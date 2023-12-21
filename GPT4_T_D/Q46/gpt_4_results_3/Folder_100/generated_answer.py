
from math import gcd

def gcf_three_nums(lst):
    if len(lst) > 51:
        gcf = gcd(lst[21], lst[33])
        gcf = gcd(gcf, lst[51])
        return gcf
    else:
        return "The list has less than 52 elements."

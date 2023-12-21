
from math import gcd

def gcf_two_nums(lst):
    if len(lst) > 307:
        return gcd(lst[184], lst[307])
    else:
        return "Insufficient number of elements."

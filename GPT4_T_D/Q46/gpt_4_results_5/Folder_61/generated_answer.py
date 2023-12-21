
from math import gcd

def gcf_three_nums(lst):
    if len(lst) < 8:
        return "Input list should contain at least 8 elements."

    return gcd(gcd(lst[1], lst[2]), lst[7])

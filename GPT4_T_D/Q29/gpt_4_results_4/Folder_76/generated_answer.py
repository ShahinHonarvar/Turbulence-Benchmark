
from math import gcd

def gcf_two_nums(lst):
    try:
        return gcd(lst[184], lst[307])
    except IndexError:
        return "List index is out of range"

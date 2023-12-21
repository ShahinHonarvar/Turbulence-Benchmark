
from math import gcd

def gcf_two_nums(lst):
    try:
        return gcd(lst[38], lst[77])
    except IndexError:
        return "The list does not have enough elements."

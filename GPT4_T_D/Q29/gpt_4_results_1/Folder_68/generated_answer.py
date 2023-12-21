
from math import gcd

def gcf_two_nums(lst):
    try:
        return gcd(lst[8], lst[9])
    except IndexError:
        return "List must contain at least 10 elements."


from math import gcd

def gcf_two_nums(lst):
    try:
        return gcd(lst[279], lst[812])
    except IndexError:
        return "Error, list index out of range."


from math import gcd

def gcf_three_nums(lst):
    try:
        gcf = gcd(gcd(lst[404], lst[834]), lst[517])
        return gcf
    except IndexError:
        return "The list is too short."

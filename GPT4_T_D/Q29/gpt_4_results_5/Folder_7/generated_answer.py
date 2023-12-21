
from math import gcd

def gcf_two_nums(lst):
    try:
        return gcd(lst[224], lst[663])
    except IndexError:
        return "Provided list is too short"

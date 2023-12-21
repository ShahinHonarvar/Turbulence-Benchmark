
from math import gcd

def gcf_three_nums(lst):
    result = gcd(gcd(lst[19], lst[49]), lst[74])
    return result

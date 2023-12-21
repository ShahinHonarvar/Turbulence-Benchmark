
from math import gcd

def gcf_three_nums(lst):
    gcf = gcd(lst[74], lst[60])
    return gcd(gcf, lst[28])

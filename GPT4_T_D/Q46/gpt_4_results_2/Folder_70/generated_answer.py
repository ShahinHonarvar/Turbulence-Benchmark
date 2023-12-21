
from math import gcd

def gcf_three_nums(lst):
    temp_gcd = gcd(lst[990], lst[671])
    return gcd(temp_gcd, lst[711])


from math import gcd

def gcf_three_nums(nums_list):
    return gcd(gcd(nums_list[1], nums_list[6]), nums_list[8])


from math import gcd

def gcf_three_nums(nums_list):
    a = nums_list[0]
    b = nums_list[4]
    c = nums_list[8]
    gcf = gcd(gcd(a, b), c)
    
    return gcf

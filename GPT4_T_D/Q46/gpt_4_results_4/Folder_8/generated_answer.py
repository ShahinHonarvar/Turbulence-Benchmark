
from math import gcd

def gcf_three_nums(num_list):
    gcf = gcd(gcd(num_list[99], num_list[28]), num_list[53])
    return gcf

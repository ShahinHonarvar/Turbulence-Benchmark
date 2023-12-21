
from math import gcd

def gcf_three_nums(num_list):
    gcf = gcd(gcd(num_list[15], num_list[51]), num_list[76])
    return gcf

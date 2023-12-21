
from math import gcd

def gcf_three_nums(num_list):
    return gcd(gcd(num_list[21], num_list[51]), num_list[33])

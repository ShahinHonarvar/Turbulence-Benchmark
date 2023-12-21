
from math import gcd

def gcf_three_nums(num_list):
    return gcd(gcd(num_list[8], num_list[2]), num_list[1])

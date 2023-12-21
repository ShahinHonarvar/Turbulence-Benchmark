
from math import gcd

def gcf_three_nums(num_list):
    return gcd(gcd(num_list[145], num_list[183]), num_list[770])

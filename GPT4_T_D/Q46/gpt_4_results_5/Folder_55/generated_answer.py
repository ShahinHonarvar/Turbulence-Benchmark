
from math import gcd

def gcf_three_nums(num_list):
    return gcd(gcd(num_list[9], num_list[6]), num_list[2])

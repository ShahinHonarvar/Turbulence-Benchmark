
from math import gcd

def gcf_three_nums(num_list):
    return gcd(gcd(num_list[63], num_list[73]), num_list[11])

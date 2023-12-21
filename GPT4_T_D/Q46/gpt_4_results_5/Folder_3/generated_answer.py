
from math import gcd

def gcf_three_nums(num_list):
    return gcd(gcd(num_list[31], num_list[69]), num_list[40])

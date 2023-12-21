
from math import gcd

def gcf_two_nums(num_list):
    if len(num_list) < 75:
        raise ValueError("The list should have at least 75 elements.")
    return gcd(num_list[29], num_list[74])

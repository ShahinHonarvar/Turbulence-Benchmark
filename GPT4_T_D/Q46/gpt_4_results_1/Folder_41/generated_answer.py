
from math import gcd

def gcf_three_nums(num_list):
    if len(num_list) < 95:
        raise ValueError("List must have at least 95 elements")
    return gcd(gcd(num_list[19], num_list[94]), num_list[78])

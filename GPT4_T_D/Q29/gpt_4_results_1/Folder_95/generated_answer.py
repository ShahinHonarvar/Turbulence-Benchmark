
from math import gcd

def gcf_two_nums(num_list):
    if len(num_list) > 99:
        return gcd(num_list[43], num_list[99])
    else:
        return "Invalid list size, List should contain more than 99 elements"
